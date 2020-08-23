from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_eoip_router = APIRouter()

@interface_eoip_router.get("/", tags=["interface"])
def get_interface_eoip(
    _id: str = "", name: str = "", mtu: str = "", actual_mtu: str = "", l2mtu: str = "", mac_address: str = "",
    arp: str = "", arp_timeout: str = "", loop_protect: str = "", loop_protect_status: str = "",
    loop_protect_send_interval: str = "", loop_protect_disable_time: str = "", local_address: str = "",
    remote_address: str = "", current_remote_address: str = "", tunnel_id: str = "", keepalive: str = "",
    dscp: str = "", clamp_tcp_mss: str = "", dont_fragment: str = "", allow_fast_path: str = "",
    running: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "name": name, "mtu": mtu, "actual-mtu": actual_mtu, "l2mtu": l2mtu,
            "mac-address": mac_address, "arp": arp, "arp-timeout": arp_timeout, "loop-protect": loop_protect,
            "loop-protect-status": loop_protect_status, "loop-protect-send-interval": loop_protect_send_interval,
            "loop-protect-disable-time": loop_protect_disable_time, "local-address": local_address,
            "remote-address": remote_address, "current-remote-address": current_remote_address,
            "tunnel-id": tunnel_id, "keepalive": keepalive, "dscp": dscp, "clamp-tcp-mss": clamp_tcp_mss,
            "dont-fragment": dont_fragment, "allow-fast-path": allow_fast_path, "running": running,
            "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "eoip")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}