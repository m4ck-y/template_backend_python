from fastapi import FastAPI
from app.health.application.unit import UnitApplication as ApplicationLayer
from app.health.infrastructure.database.implementation.unit import UnitRepository as repository
from app.health.infrastructure.service.routes.unit import setup_service, router

def setup(api_server: FastAPI):
    print("setup >>> unit")
    repo = repository()
    app = ApplicationLayer(repo)
    setup_service(app)
    print("Registrando rutas de unidad...")
    api_server.include_router(router)
    print("unit_router", router)
    print("api_server", api_server)
    print(api_server.routes)
    print("Rutas de unidad registradas.")