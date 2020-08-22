from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_bridge_msti_router = APIRouter()

@interface_bridge_msti_router.get("/")
def get_interface_bridge_msti(
    _id: str = "", identifier: str = "", bridge: str = "", priority: str = "", vlan_mapping: str = "",
    disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "identifier": identifier, "bridge": bridge, "priority": priority,
            "vlan-mapping": vlan_mapping, "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "bridge", "msti")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}