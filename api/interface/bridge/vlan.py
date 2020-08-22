from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

vlan_router = APIRouter()

@vlan_router.get("/")
def get_interface_bridge_vlan(
    _id: str = "", bridge: str = "", vlan_ids: str = "", tagged: str = "", untagged: str = "",
    current_tagged: str = "", current_untagged: str = "", dynamic: str = "", disabled: str = ""
    ):
    try:
        filters_dict = {
            ".id": _id, "bridge": bridge, "vlan-ids": vlan_ids, "tagged": tagged, "untagged": untagged,
            "current-tagged": current_tagged, "current-untagged": current_untagged, "dynamic": dynamic,
            "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "bridge", "vlan")
        data = data.select(*filters_dict.keys()).where(*filters_list)
        
        return tuple(data)

    except Exception as e:
        return {"error": e}