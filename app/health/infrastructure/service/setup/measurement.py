from fastapi import FastAPI
from app.utils.application.base import BaseLayerApplication as LayerApplication
from app.health.infrastructure.database.implementation.measurement import MeasurementRepository as LayerRepository
from app.health.infrastructure.service.routes.measurement import ServiceMeasurement as LayerService


def setup(api_server: FastAPI):
    print("setup >>> measurement")
    repo = LayerRepository()
    app = LayerApplication(repo)
    LayerService(api_server,app, "health")