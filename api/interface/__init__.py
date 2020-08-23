from fastapi import APIRouter

from ._root import _root_router
from .interface_list import interface_list_router
from .interface_list_member import interface_list_member_router
from .interface_ethernet import interface_ethernet_router
from .interface_eoip import interface_eoip_router
from .interface_ipip import interface_ipip_router
from .interface_gre import interface_gre_router
from .interface_vlan import interface_vlan_router
from .interface_vrrp import interface_vrrp_router
from .interface_bonding import interface_bonding_router
from .bridge import bridge_router
from .wireless import wireless_router

interface_router = APIRouter()

interface_router.include_router(
    _root_router,
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

interface_router.include_router(
    interface_vlan_router,
    prefix="/vlan"
)

interface_router.include_router(
    interface_vrrp_router,
    prefix="/vrrp"
)

interface_router.include_router(
    interface_bonding_router,
    prefix="/bonding"
)

interface_router.include_router(
    bridge_router,
    prefix="/bridge"
)

interface_router.include_router(
    wireless_router,
    prefix="/wireless"
)