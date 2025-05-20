from fastapi import APIRouter
from app.health.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaCreateUnit as C,
    SchemaUpdateUnit as U,
)
from app.utils.application.base import BaseLayerApplication
from app.utils.infrastructure.service.base import BaseLayerService

ROUTE_NAME = "unit"

class ServiceUnit(BaseLayerService[E, C, U]):
    def __init__(self, router: APIRouter, app_layer: BaseLayerApplication, route_parent: str = None):
        super().__init__(router, app_layer, C, U, E, ROUTE_NAME, route_parent)