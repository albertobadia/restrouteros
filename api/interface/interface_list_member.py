from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_list_member_router = APIRouter()

@interface_list_member_router.get("/", tags=["interface"])
def get_interface_list_member(
    _id: str = "", _list: str = "", interface: str = "", dynamic: str = "", disabled: str = ""
    ):
    try:

        filters_dict = {
            ".id": _id,
            "list": _list,
            "interface": interface,
            "dynamic": dynamic,
            "disabled": disabled
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "list", "member")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)

    except Exception as e:
        return {"error": e}