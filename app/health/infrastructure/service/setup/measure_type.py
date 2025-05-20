from fastapi import FastAPI
from app.utils.application.base import BaseLayerApplication as LayerApplication
from app.health.infrastructure.database.implementation.measure_type import MeasureTypeRepository as LayerRepository
from app.health.infrastructure.service.routes.measure_type import ServiceMeasureType as LayerService


def setup(api_server: FastAPI):
    print("setup >>> measure_type")
    repo = LayerRepository()
    app = LayerApplication(repo)
    LayerService(api_server,app)