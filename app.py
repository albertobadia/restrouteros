from fastapi import FastAPI
from api.tags_metadata import tags_metadata

APP = FastAPI(
    title="RestRouterOS",
    description="Adds the power of RestAPI to Mikrotik RouterOS",
    version=20200819,
    openapi_tags=tags_metadata
)