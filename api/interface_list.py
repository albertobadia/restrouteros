from fastapi import APIRouter
from librouteros.query import Key
from device import DEVICE
from api import get_filters_list

interface_list_router = APIRouter()

@interface_list_router.get("/")
def get_interface_list(
    _id: str = "", name: str = "", dynamic: str = "", include: str = "", exclude: str = "",
    builtin: str = "", comment: str = ""
    ):

    try:

        filters_dict = {
            ".id": _id,
            "name": name,
            "dynamic": dynamic,
            "include": include,
            "exclude": exclude,
            "builtin": builtin,
            "comment": comment
        }

        filters_list = get_filters_list(filters_dict=filters_dict)

        data = DEVICE.path("interface", "list")
        data = data.select(*filters_dict.keys()).where(*filters_list)

        return tuple(data)
    
    except Exception as e:
        return {"error": e}