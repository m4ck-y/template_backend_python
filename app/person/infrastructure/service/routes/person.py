from fastapi import FastAPI
from app.person.domain.schemas.person import (
    SchemaCreateAPIPerson as C,
    SchemaItemPerson as I,
    SchemaDetailPerson as E,
    SchemaPersonUpdate as U,
)
from app.utils.application.base import BaseLayerApplication
from app.utils.infrastructure.service.base import BaseLayerService

ROUTE_NAME = "person"

class ServicePerson(BaseLayerService[C, I, E, U]):
    def __init__(self, router: FastAPI, app_layer: BaseLayerApplication, route_parent: str = None):
        super().__init__(router, app_layer, C, I, E, U, ROUTE_NAME, route_parent)
