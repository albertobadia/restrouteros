from fastapi import APIRouter
from ._root import _root_router

wireless_router = APIRouter()

wireless_router.include_router(
    _root_router,
    prefix=""
)