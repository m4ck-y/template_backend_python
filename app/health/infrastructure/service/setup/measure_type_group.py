from fastapi import FastAPI
from app.utils.application.base import BaseLayerApplication as LayerApplication
from app.health.infrastructure.database.implementation.measure_type_group import MeasureTypeGroupRepository as LayerRepository
from app.health.infrastructure.service.routes.measure_type_group import ServiceMeasureTypeGroup as LayerService


def setup(api_server: FastAPI):
    print("setup >>> measure_type_group")
    repo = LayerRepository()
    app = LayerApplication(repo)
    LayerService(api_server,app, "health")