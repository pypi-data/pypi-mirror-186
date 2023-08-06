import re
import logging
from typing import Any, Optional, List, Union
from dataclasses import dataclass
from ipaddress import IPv4Address

from netaddr import EUI
import ncs


@dataclass
class MACTableEntry:
    """
    Represents a normalized entry in any given devices' MAC address table
    """

    address: EUI  # EUI("cc:88:c7:cc:16:ac", dialect=mac_unix_expanded)
    interface: str  # "Gi1/0", "ge-0/0/18", etc
    vlan_id: Optional[int] = None  # range(1, 4096)


@dataclass
class ARPTableEntry:
    """
    Represents a normalized entry in any given devices' ARP table
    """

    ip_address: IPv4Address
    mac_address: EUI  # EUI("cc:88:c7:cc:16:ac", dialect=mac_unix_expanded)
    interface: str  # "Gi1/0", "ge-0/0/18", etc
    vrf: Optional[str] = None


@dataclass
class Interface:
    """
    Represents normalized operation data about a device interface
    """

    name: str  # inteface id, e.g. "ge-0/0/18" or "Gi1/0"
    admin_status: str  # "enabled" or "disabled"
    oper_status: str  # "up" or "down"
    duplex: str  # auto/half/full
    speed: str  # 10/100/1000/auto
    is_logical: bool = False  # software interfaces (Vlan,irb, etc) set to True
    description: Optional[str] = None  # e.g. "1401A: hallway printer"


@dataclass
class LLDPNeighbor:
    """
    Represents a normalized LLDP neighbor table entry
    """
    local_interface: str  # interface id, e.g. "ge-0/0/18" or "Gi1/0"
    remote_interface: str  # interface id, e.g. "ge-0/0/18" or "Gi1/0"
    remote_system_name: str  # hostname of connected device
    remote_system_description: Optional[str] = None  # description of connected device


class BaseDevice:
    def __init__(self, device: ncs.maagic.Node, log: logging.Logger):
        self.device = device
        self.log = log

    @staticmethod
    def normalize_mac(mac: str) -> str:
        mac = re.sub(r"[\.\-\:]", "", mac)
        return f"{mac[0:2]}:{mac[2:4]}:{mac[4:6]}:{mac[6:8]}:{mac[8:10]}:{mac[10:12]}"

    def _run_cmd(self, command: str) -> Any:
        raise NotImplementedError

    def get_mac_table(self, mac: Optional[str] = None) -> List[MACTableEntry]:
        raise NotImplementedError

    def get_arp_table(
        self, address: Optional[str] = None, vrf: Optional[str] = None
    ) -> List[ARPTableEntry]:
        raise NotImplementedError

    def get_interface_details(self, interface: Optional[str] = None) -> List[Interface]:
        raise NotImplementedError

    def get_bfd_neighbors(self, interface: Optional[str] = None) -> Any:
        raise NotImplementedError

    def get_ospf_neighbors(self, interface: Optional[str] = None) -> Any:
        raise NotImplementedError

    def get_lldp_neighbors(self, interface: Optional[str] = None) -> List[LLDPNeighbor]:
        raise NotImplementedError

    def get_transceiver_details(self, interface: Optional[str] = None) -> Any:
        raise NotImplementedError
