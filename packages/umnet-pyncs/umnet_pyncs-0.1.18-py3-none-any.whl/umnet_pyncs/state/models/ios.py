from typing import List, Optional
from ipaddress import IPv4Address

from ntc_templates.parse import parse_output
from netaddr import EUI, mac_unix_expanded

from .base import BaseDevice, ARPTableEntry, MACTableEntry, Interface, LLDPNeighbor


# note that since we're using 'show int status',
# admin and oper status leverage the same output column, whose values can be:
#  - connected (admin up, oper up)
#  - notconnect (admin up, oper down)
#  - disabled (admin down, oper down)
#  - suspended (admin up, oper down)
#  - err-disabled (admin up, oper down)
ADMIN_STATUS = {
    "connected": "enabled",
    "notconnect": "enabled",
    "disabled": "disabled",
    "suspended": "enabled",
    "err-disabled": "enabled",
}
OPER_STATUS = {
    "connected": "up",
    "notconnect": "down",
    "disabled": "down",
    "suspended": "down",
    "err-disabled": "down",
}
DUPLEX = {
    "half": "half",
    "full": "full",
    "auto": "full",
    "a-half": "half",
    "a-full": "full",
}
SPEED = {
    "10": "10",
    "100": "100",
    "1000": "1000",
    "10G": "auto",
    "auto": "auto",
    "a-10": "10",
    "a-100": "100",
    "a-1000": "1000",
    "a-2500": "2500",
    "a-10G": "auto",
}
INTERFACE_PREFIX_MAP = {
    "FastEthernet": "Fa",
    "GigabitEthernet": "Gi",
    "TenGigabitEthernet": "Te",
}


def _remove_prompt(results: str) -> str:
    """
    remove the trailing prompt from the results of a live_status show
    command.  This only appears to be an issue for the IOS NED. i.e:

    ...
    Gi2/0/48        notconnect   1       auto   auto 10/100/1000BaseTX
    Twe2/1/1        connected    1       full    10G SFP-10GBase-SR
    Twe2/1/2        notconnect   1       auto   auto unknown
    Ap2/0/1         connected    1     a-full a-1000 App-hosting port
    al-shallow-1#    <-- (rude)
    """
    lines = results.splitlines()
    try:
        del lines[-1]
    except IndexError:
        pass
    return "\n".join(lines)


def _normalize_ifname(name: str) -> str:
    """
    Some IOS platforms return fully-qualified interface identifiers, e.g.
    'GigabitEthernet1/1' whereas others use abbreviated names e.g. 'Gi1\1'.
    Since the NCS switchport services uses abbreviated versions for IOS,
    this function will convert the names returned by the device to the
    shortened version
    """
    if name.startswith("FastEthernet"):
        newname = "Fa" + name.split("FastEthernet")[1]
    elif name.startswith("GigabitEthernet"):
        newname = "Gi" + name.split("GigabitEthernet")[1]
    elif name.startswith("TenGigabitEthernet"):
        newname = "Te" + name.split("TenGigabitEthernet")[1]
    else:
        return name

    return newname


class IOS(BaseDevice):
    def _run_cmd(self, command: str) -> str:
        """
        use NCS live-status exec to issue a raw show command towards a device.
        platform-specific models are expected to parse this output and return
        structured data.

        :param command: string CLI command, e.g. 'show interface status'
        :returns: raw string output from the device
        """
        show = self.device.live_status.__getitem__("exec").show
        inp = show.get_input()
        inp.args = [command]

        results = show.request(inp)

        return _remove_prompt(results.result)

    def get_interface_details(self, interface: Optional[str] = None) -> List[Interface]:
        """
        Gathers interface operational data from an IOS device by parsing 'show interfaces status'

        :interface: optionally get data only for a single interface

        see the ntc_templates test data for this template for details on output structure:
        https://github.com/networktocode/ntc-templates/tree/master/tests/cisco_ios/show_interfaces_status

        ---
        parsed_sample:
          - port: "Gi1/0/1"
            name: ""
            status: "notconnect"
            vlan: "1"
            duplex: "auto"
            speed: "auto"
            type: "10/100/1000BaseTX"
            fc_mode: ""
        """
        # ncs automatically adds the 'show' to the front of the cmd
        command = f"interfaces {interface} status" if interface else "interfaces status"
        self.log.debug(f"sending 'show {command}' to {self.device.name}")
        reply = self._run_cmd(command)
        # self.log.debug(f" <<<{ self.device.name }>>>: {reply.result}")

        parsed = parse_output(
            platform="cisco_ios",
            command="show interfaces status",
            data=reply,
        )

        ret = []
        for entry in parsed:
            record = Interface(
                name=entry["port"],
                description=entry["name"],
                admin_status=ADMIN_STATUS[entry["status"]],
                oper_status=OPER_STATUS[entry["status"]],
                duplex=DUPLEX[entry["duplex"]],
                speed=SPEED.get(entry["speed"], "auto"),
            )

            if record.name.startswith("Vlan"):
                record.is_logical = True

            ret.append(record)

        return ret

    def get_arp_table(
        self, address: Optional[str] = None, vrf: Optional[str] = None
    ) -> List[ARPTableEntry]:
        """
        Gathers ARP data from an IOS device by parsing the output of the CLI
        command 'show ip arp [ address | vrf <VRF>]'

        :address: optionally filter device output by MAC or IP address
        :vrf: optional string name of VRF table to look in

        see the ntc_templates test data for this template for details on output structure:
        https://github.com/networktocode/ntc-templates/tree/master/tests/cisco_ios/show_ip_arp

        TODO: add support(recursion?) for vrf='all' since ios makes you run a separate
              lookup command for every vrf (so rude)

        ---
        parsed_sample:
          - protocol: "Internet"
            address: "172.16.233.229"
            age: "-"
            mac: "0000.0c59.f892"
            type: "ARPA"
            interface: "Ethernet0/0"
        """
        # ncs automatically adds the 'show' to the front of the cmd
        command = "ip arp"
        if vrf is not None:
            command = command + f" vrf {vrf}"
        if address is not None:
            command = command + f" address {address}"
            normalized_address = IPv4Address(address)

        self.log.debug(f"sending 'show {command}' to {self.device.name}")
        reply = self._run_cmd(command)
        # self.log.debug(f" <<<{ self.device.name }>>>: {reply.result}")

        parsed = parse_output(
            platform="cisco_ios",
            command="show ip arp",
            data=reply,
        )

        ret = []
        for entry in parsed:
            if entry["mac"] == "Incomplete":
                continue

            normalized_entry_address = IPv4Address(entry["address"])

            if address is None or normalized_address == normalized_entry_address:
                record = ARPTableEntry(
                    ip_address=IPv4Address(entry["address"]),
                    mac_address=EUI(entry["mac"], dialect=mac_unix_expanded),
                    interface=entry["interface"],
                    vrf=vrf,
                )
                ret.append(arp)

        return ret

    def get_mac_table(self, mac: Optional[str] = None) -> List[MACTableEntry]:
        """
        Gathers dynamically-learned MAC address data from an IOS device by
        parsing the output of the CLI command 'show mac address-table dynamic
        [address <address>]'

        :mac: optionally filter device output by MAC address

        see the ntc_templates test data for this template for details on output structure:
        https://github.com/networktocode/ntc-templates/tree/master/tests/cisco_ios/show_mac-address-table

        ---
        parsed_sample:
        - destination_address: "30a3.30a3.a1c3"
            type: "dynamic"
            vlan: "666"
            destination_port:
            - "Te1/30"
        """
        # ncs automatically adds the 'show' to the front of the cmd
        command = "mac address-table dynamic"
        if mac is not None:
            normalized_mac = EUI(mac, dialect=mac_unix_expanded)
            command = command + f" address {mac}"

        self.log.debug(f"sending 'show {command}' to {self.device.name}")
        reply = self._run_cmd(command)
        # self.log.debug(f" <<<{ self.device.name }>>>: {reply.result}")

        parsed = parse_output(
            platform="cisco_ios",
            command="show mac-address-table",
            data=reply,
        )

        ret = []
        for entry in parsed:
            try:
                vid = int(entry["vlan"])
            except ValueError:
                vid = None

            normalized_entry_mac = EUI(
                entry["destination_address"], dialect=mac_unix_expanded
            )
            # unless there's an on-going broadcast storm we should only be
            # learning an address on a single port -- not sure why the template
            # is modelled this way?
            interface = _normalize_ifname(entry["destination_port"][0])

            if mac is None or normalized_mac == normalized_entry_mac:
                record = MACTableEntry(
                    address=normalized_entry_mac,
                    vlan_id=vid,
                    interface=interface,
                )
                ret.append(record)

        return ret

    def get_lldp_neighbors(self, interface: Optional[str] = None) -> List[LLDPNeighbor]:
        """
        Gathers active LLDP neighbors from an IOS device by
        parsing the output of the CLI command 'show lldp neighbors detail'

        :interface: optionally filter device output by interface

        see the ntc_templates test data for this template for details on output structure:
        https://github.com/networktocode/ntc-templates/blob/master/tests/cisco_ios/show_lldp_neighbors_detail/cisco_ios_show_lldp_neighbors_detail1.yml

        ---
        parsed_sample:
        - local_interface: "Gi1/0/2"
          chassis_id: "7c25.86c9.aaaa"
          neighbor_port_id: "502"
          neighbor_interface: "ge-0/0/0.0"
          neighbor: ""
          system_description: "Juniper Networks, Inc. ex2200-24t-4g , version 12.3R9.4 Build\
          \ date: 2015-02-12 11:25:30 UTC"
          capabilities: "B,R"
          management_ip: ""
          vlan: "1"
          serial: ""
          power_pair: ""
          power_class: ""
          power_device_type: ""
          power_priority: ""
          power_source: ""
          power_requested: ""
        """
        # ncs automatically adds the 'show' to the front of the cmd
        command = "lldp neighbors"

        self.log.debug(f"sending 'show {command}' to {self.device.name}")
        reply = self._run_cmd(command)
        # self.log.debug(f" <<<{ self.device.name }>>>: {reply.result}")

        parsed = parse_output(
            platform="cisco_ios",
            command="show lldp neighbors",
            data=reply,
        )

        ret = []
        for entry in parsed:
            record = LLDPNeighbor(
                local_interface=entry["local_interface"],
                remote_interface=entry["neighbor_interface"],
                remote_system_name=entry["neighbor"],
            )
            if interface is None or entry["local_interface"] == interface:
                ret.append(record)

        return ret
