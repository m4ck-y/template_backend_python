from fastapi import FastAPI
from app.account.domain.schemas.user import (
    SchemaCreateAPIUser as C,
    SchemaItemUser as I,
    SchemaDetailUser as E,
    SchemaUserUpdate as U
)

from app.utils.application.base import BaseLayerApplication
from app.utils.infrastructure.service.base import BaseLayerService

ROUTE_NAME = "user"

class ServiceUser(BaseLayerService[C, I, E, U]):
    def __init__(self, router: FastAPI, app_layer: BaseLayerApplication, route_parent: str = None):
        super().__init__(router, app_layer, C, I, E, U, ROUTE_NAME, route_parent)