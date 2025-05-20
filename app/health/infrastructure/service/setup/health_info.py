from fastapi import FastAPI
from app.utils.application.base import BaseLayerApplication as LayerApplication
from app.health.infrastructure.database.implementation.health_info import HealthInfoRepository as LayerRepository
from app.health.infrastructure.service.routes.health_info import ServiceHealthInfo as LayerService


def setup(api_server: FastAPI):
    print("setup >>> health_info")
    repo = LayerRepository()
    app = LayerApplication(repo)
    LayerService(api_server,app)