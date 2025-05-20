from fastapi import APIRouter
from app.health.domain.schemas.measure_group import (
    SchemaMeasureGroup as E,
    SchemaCreateMeasureGroup as C,
    SchemaUpdateMeasureGroup as U,
)
from app.utils.application.base import BaseLayerApplication
from app.utils.infrastructure.service.base import BaseLayerService

ROUTE_NAME = "measure_group"

class ServiceMeasureGroup(BaseLayerService[E, C, U]):
    def __init__(self, router: APIRouter, app_layer: BaseLayerApplication, route_parent: str = None):
        route_name = f"{route_parent}/{ROUTE_NAME}" if route_parent else ROUTE_NAME
        super().__init__(router, app_layer, C, U, E, route_name)