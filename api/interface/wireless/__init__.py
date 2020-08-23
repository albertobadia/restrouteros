from fastapi import APIRouter
from ._root import _root_router
from .nstreme_dual import nstreme_dual_router
from .access_list import access_list_router
from .registration_table import registration_table_router

wireless_router = APIRouter()

wireless_router.include_router(
    _root_router,
    prefix=""
)

wireless_router.include_router(
    nstreme_dual_router,
    prefix="/nstreme-dual"
)

wireless_router.include_router(
    access_list_router,
    prefix="/access-list"
)

wireless_router.include_router(
    registration_table_router,
    prefix="/registration-table"
)