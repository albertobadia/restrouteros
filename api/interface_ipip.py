from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_ipip_router = APIRouter()

@interface_ipip_router.get("/")
def get_interface_ipip(
    _id: str = "", name: str = "", mtu: str = "", actual_mtu: str = "", local_address: str = "",
    remote_address: str = "", current_remote_address: str = "", keepalive: str = "", dscp: str = "",
    clamp_tcp_mss: str = "", dont_fragment: str = "", allow_fast_path: str = "", running: str = "",
    disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "name": name, "mtu": mtu, "actual-mtu": actual_mtu, "local-address": local_address,
            "remote-address": remote_address, "current-remote-address": current_remote_address,
            "keepalive": keepalive, "dscp": dscp, "clamp-tcp-mss": clamp_tcp_mss, "dont-fragment": dont_fragment,
            "allow-fast-path": allow_fast_path, "running": running, "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "ipip")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}
