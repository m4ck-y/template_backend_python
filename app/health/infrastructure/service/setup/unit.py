from fastapi import FastAPI
from app.health.application.unit import UnitApplication as LayerApplication
from app.health.infrastructure.database.implementation.unit import UnitRepository as LayerRepository
from app.health.infrastructure.service.routes.unit import ServiceUnit as LayerService

def setup(api_server: FastAPI):
    print("setup >>> unit")
    repo = LayerRepository()
    app = LayerApplication(repo)
    LayerService(api_server,app, "health")