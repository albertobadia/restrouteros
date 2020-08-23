from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_vlan_router = APIRouter()

@interface_vlan_router.get("/", tags=["interface"])
def get_interface_vlan(
    _id: str = "", name: str = "", mtu: str = "", l2mtu: str = "", mac_address: str = "", arp: str = "",
    arp_timeout: str = "", loop_protect: str = "", loop_protect_status: str = "",
    loop_protect_send_interval: str = "", loop_protect_disable_time: str = "", vlan_id: str = "",
    interface: str = "", use_service_tag: str = "", running: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "name": name, "mtu": mtu, "l2mtu": l2mtu, "mac-address": mac_address, "arp": arp,
            "arp-timeout": arp_timeout, "loop-protect": loop_protect, "loop-protect-status": loop_protect_status,
            "loop-protect-send-interval": loop_protect_send_interval,
            "loop-protect-disable-time": loop_protect_disable_time, "vlan-id": vlan_id, "interface": interface,
            "use-service-tag": use_service_tag, "running": running, "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "vlan")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}