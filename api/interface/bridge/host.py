from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

host_router = APIRouter()

@host_router.get("/", tags=["bridge"])
def get_interface_bridge_host(
    _id: str = "", mac_address: str = "", interface: str = "", bridge: str = "", on_interface: str = "",
    age: str = "", invalid: str = "", dynamic: str = "", local: str = "", external: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "mac-address": mac_address, "interface": interface, "bridge": bridge,
            "on-interface": on_interface, "age": age, "invalid": invalid, "dynamic": dynamic, "local": local,
            "external": external, "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "bridge", "host")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}