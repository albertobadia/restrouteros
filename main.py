from app import APP
from api.interface import interface_router
from api.interface_list import interface_list_router
from api.interface_list_member import interface_list_member_router
from api.interface_ethernet import interface_ethernet_router
from api.interface_eoip import interface_eoip_router
from api.interface_ipip import interface_ipip_router

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

APP.include_router(
    interface_eoip_router,
    prefix="/interface/eoip"
)

APP.include_router(
    interface_ipip_router,
    prefix="/interface/ipip"
)