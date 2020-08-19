from app import APP

from api.interface import interface_router

APP.include_router(
    interface_router,
    prefix="/interface"
)