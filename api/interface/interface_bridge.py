from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_bridge_router = APIRouter()

@interface_bridge_router.get("/")
def get_interface_bridge(
    _id: str = "", name: str = "", mtu: str = "", actual_mtu: str = "", l2mtu: str = "", arp: str = "",
    arp_timeout: str = "", mac_address: str = "", protocol_mode: str = "", fast_forward: str = "",
    igmp_snooping: str = "", auto_mac: str = "", ageing_time: str = "", vlan_filtering: str = "",
    dhcp_snooping: str = "", running: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "name": name, "mtu": mtu, "actual-mtu": actual_mtu, "l2mtu": l2mtu, "arp": arp,
            "arp-timeout": arp_timeout, "mac-address": mac_address, "protocol-mode": protocol_mode,
            "fast-forward": fast_forward, "igmp-snooping": igmp_snooping, "auto-mac": auto_mac,
            "ageing-time": ageing_time, "vlan-filtering": vlan_filtering, "dhcp-snooping": dhcp_snooping,
            "running": running, "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "bridge")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}