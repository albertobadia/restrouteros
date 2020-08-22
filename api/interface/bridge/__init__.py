from fastapi import APIRouter
from ._root import _root_router
from .port import port_router
from .vlan import vlan_router
from .msti import msti_router
from .filter import filter_router
from .nat import nat_router
from .host import host_router

bridge_router = APIRouter()


bridge_router.include_router(
    _root_router,
    prefix=""
)

bridge_router.include_router(
    port_router,
    prefix="/port"
)

bridge_router.include_router(
    vlan_router,
    prefix="/vlan"
)

bridge_router.include_router(
    msti_router,
    prefix="/msti"
)

bridge_router.include_router(
    filter_router,
    prefix="/filter"
)

bridge_router.include_router(
    nat_router,
    prefix="/nat"
)

bridge_router.include_router(
    host_router,
    prefix="/host"
)