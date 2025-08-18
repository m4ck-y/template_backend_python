from fastapi import APIRouter
from app.health.domain.schemas.health_info import (
    SchemaHealthInfo as E,
    SchemaCreateHealthInfo as C,
    SchemaUpdateHealthInfo as U,
)
from app.utils.application.base import BaseLayerApplication
from app.utils.infrastructure.service.base import BaseLayerService

ROUTE_NAME = "health_info"

class ServiceHealthInfo(BaseLayerService[E, C, U]):
    def __init__(self, router: APIRouter, app_layer: BaseLayerApplication, route_parent: str = None):
        super().__init__(router, app_layer, C, U, E, ROUTE_NAME, route_parent)