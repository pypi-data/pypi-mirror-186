# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['umnet_pyncs', 'umnet_pyncs.state', 'umnet_pyncs.state.models']

package_data = \
{'': ['*']}

install_requires = \
['multiprocessing-logging>=0.3.3,<0.4.0',
 'netaddr>=0.8.0,<0.9.0',
 'ntc-templates>=3.0.0,<4.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata==6.0.0']}

setup_kwargs = {
    'name': 'umnet-pyncs',
    'version': '0.1.18',
    'description': 'custom python module for NCS helpers',
    'long_description': '## Overview\n\nThis module is intended to be installed on the production NCS nodes and imported in other services/actions that need to gather state from the network.  It uses the NCS device manager and the standard python `multiprocessing` library to connect to devices in-parallel and issue commands, returning results as structured data.\n\n## Usage information\n\nBasic usage example in an NCS callback:\n\n``` python\nfrom umnet_pyncs.state import StateManager\n...\n\n\nclass DemoAction(Action):\n    @Action.action\n    def cb_action(self, uinfo, name, kp, input, output, trans):\n        ...\n        with StateManager() as m:\n            interfaces = m.get_state(al_devices, ["get-interface-details"])\n            arp = m.get_state(dl_devices, ["get-arp-table"])\n            ...\n```\n\n## Supported commands\n\nCurrently supported commands are:\n- `get-mac-table`\n- `get-arp-table`\n- `get-interface-details`\n- `get-transciever-details`\n- `get-lldp-neighbors`\n- `get-bfd-neighbors`\n- `get-ospf-neighbors`\n\n## Developer testing\n\nInstall the [ncs-pycli](https://pypi.org/project/ncs-pycli/) package into your local NSO development environment.  Run `ncs_pycli` to get an ipython shell with an open transaction:\n\n``` python\nimport logging\nfrom umnet_pyncs.state import StateManager\n\nlog = logging.getLogger()\nlog.setLevel(logging.DEBUG)\n\ndevices = [d for d in root.devices.device]\n\nm = StateManager()\n\ninterfaces = m.get_state(devices, ["get-interface-details"])\n    \nprint(interfaces)\n\nm.__exit__()\n```\n\nFor any given command, the various platform-specific models are responsible for implementing how the data is fetched and parsed from the remote device.  Each command corresponds to a method that can be invoked to retrieve the data, e.g. `get-interface-details` maps to the `get_interface_details()` instance method of the model(s).\n\nFor Cisco IOS and NXOS devices (which use CLI-based NEDs), the built-in NCS `live-status` action(s) are used to send raw CLI commands to the device.  For example, the `get_mac_address()` method will send a `show mac address-table` CLI command.  For both IOS and NXOS we use [ntc_templates](https://github.com/networktocode/ntc-templates) to parse the raw text output into structured data.\n\nFor Juniper devices, since the NED uses NETCONF for all device communications, we instead call the `<get-ethernet-switching-table-information>` RPC directly.  Since this RPC is modelled in YANG, we can then parse the results directly using the maagic API.\n\nAll the nitty-gritty details of parsing the data retrieved directly from the remote device is handled by the platform-specific model implementation for that device.  Each model normalizes the data using the dataclasses defined in [base.py](./umnet_pyncs/state/models/base.py).  The intention is to makes it simpler for NCS actions/services to use this module, as well as making it easier to develop/maintain.\n\n**NB**: this implementation currently relies on an additional template for NXOS that handles parsing `show ip arp detail vrf all` -- see [PR# 1204](https://github.com/networktocode/ntc-templates/pull/1204).\n',
    'author': 'Nick Grundler',
    'author_email': 'grundler@umich.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
