from fastapi import APIRouter

from .interface import interface_router
from .interface_list import interface_list_router
from .interface_list_member import interface_list_member_router
from .interface_ethernet import interface_ethernet_router
from .interface_eoip import interface_eoip_router
from .interface_ipip import interface_ipip_router
from .interface_gre import interface_gre_router

interface_router = APIRouter()

interface_eoip_router.include_router(
    interface_router,
    prefix=""
)

interface_router.include_router(
    interface_list_router,
    prefix="/list"
)

interface_router.include_router(
    interface_list_member_router,
    prefix="/list/member"
)

interface_router.include_router(
    interface_ethernet_router,
    prefix="/ethernet"
)

interface_router.include_router(
    interface_eoip_router,
    prefix="/eoip"
)

interface_router.include_router(
    interface_ipip_router,
    prefix="/ipip"
)

interface_router.include_router(
    interface_gre_router,
    prefix="/gre"
)