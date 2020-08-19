from app import APP
from api.interface import interface_router
from api.interface_list import interface_list_router
from api.interface_list_member import interface_list_member_router
from api.interface_ethernet import interface_ethernet_router

APP.include_router(
    interface_router,
    prefix="/interface"
)

APP.include_router(
    interface_list_router,
    prefix="/interface/list"
)

APP.include_router(
    interface_list_member_router,
    prefix="/interface/list/member"
)

APP.include_router(
    interface_ethernet_router,
    prefix="/interface/ethernet"
)