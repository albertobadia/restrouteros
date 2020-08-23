from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

nat_router = APIRouter()

@nat_router.get("/", tags=["bridge"])
def get_interface_bridge_nat(
    _id: str = "", chain: str = "", action: str = "", log: str = "", log_prefix: str = "", bytes: str  = "",
    packets: str = "", invalid: str = "", dynamic: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "chain": chain, "action": action, "log": log, "log-prefix": log_prefix, "bytes": bytes,
            "packets": packets, "invalid": invalid, "dynamic": dynamic, "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "bridge", "nat")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}