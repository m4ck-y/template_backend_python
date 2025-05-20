from fastapi import FastAPI
from app.person.domain.schemas.person import (
    SchemaPerson as E,
    SchemaPersonCreate as C,
    SchemaPersonUpdate as U,
)
from app.utils.application.base import BaseLayerApplication
from app.utils.infrastructure.service.base import BaseLayerService

ROUTE_NAME = "person"

class ServicePerson(BaseLayerService[C, U, E]):
    def __init__(self, router: FastAPI, app_layer: BaseLayerApplication, route_parent: str = None):
        route_name = f"{route_parent}/{ROUTE_NAME}" if route_parent else ROUTE_NAME
        super().__init__(router, app_layer, C, U, E, route_name)
