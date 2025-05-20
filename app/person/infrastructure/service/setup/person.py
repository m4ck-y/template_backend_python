from fastapi import FastAPI
from app.person.application.person import PersonApplication as LayerApplication
from app.person.infrastructure.database.implementation.person import PersonRepository as LayerRepository
from app.person.infrastructure.service.routes.person import ServicePerson as LayerService

def setup_person(api_server: FastAPI):
    print("setup >>> person")
    repo = LayerRepository()
    app = LayerApplication(repo)
    LayerService(api_server, app)