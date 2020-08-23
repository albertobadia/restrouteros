from fastapi import APIRouter
from ._root import _root_router
from .nstreme_dual import nstreme_dual_router

wireless_router = APIRouter()

wireless_router.include_router(
    _root_router,
    prefix=""
)

wireless_router.include_router(
    nstreme_dual_router,
    prefix="/nstreme-dual"
)