from fastapi import APIRouter

from .interface import interface_router
from .interface_list import interface_list_router
from .interface_list_member import interface_list_member_router
from .interface_ethernet import interface_ethernet_router
from .interface_eoip import interface_eoip_router
from .interface_ipip import interface_ipip_router
from .interface_gre import interface_gre_router
from .interface_vlan import interface_vlan_router
from .interface_vrrp import interface_vrrp_router
from .interface_bonding import interface_bonding_router
from .interface_bridge import interface_bridge_router
from .interface_bridge_port import interface_bridge_port_router
from .interface_bridge_vlan import interface_bridge_vlan_router
from .interface_bridge_msti import interface_bridge_msti_router
from .interface_bridge_filter import interface_bridge_filter_router
from .interface_bridge_nat import interface_bridge_nat_router


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
    interface_bridge_router,
    prefix="/bridge"
)

interface_router.include_router(
    interface_bridge_port_router,
    prefix="/bridge/port"
)

interface_router.include_router(
    interface_bridge_vlan_router,
    prefix="/bridge/vlan"
)

interface_router.include_router(
    interface_bridge_msti_router,
    prefix="/bridge/msti"
)

interface_router.include_router(
    interface_bridge_filter_router,
    prefix="/bridge/filter"
)

interface_router.include_router(
    interface_bridge_nat_router,
    prefix="/bridge/nat"
)