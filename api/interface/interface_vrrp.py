from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_vrrp_router = APIRouter()

@interface_vrrp_router.get("/", tags=["interface"])
def get_interface_vrrp(
    _id: str = "", name: str = "", mtu: str = "", mac_address: str = "", arp: str = "", arp_timeout: str = "",
    interface: str = "", vrid: str = "", priority: str = "", interval: str = "", preemption_mode: str = "",
    authentication: str = "", password: str = "", on_backup: str = "", on_master: str = "", version: str = "",
    v3_protocol: str = "", invalid: str = "", running: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "name": name, "mtu": mtu, "mac-address": mac_address, "arp": arp,
            "arp-timeout": arp_timeout, "interface": interface, "vrid": vrid, "priority": priority,
            "interval": interval, "preemption-mode": preemption_mode, "v3-protocol": v3_protocol,
            "invalid": invalid, "running": running, "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "vrrp")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}