from fastapi import FastAPI
from app.account.application.user import UserApplication as LayerApplication
from app.account.infrastructure.database.implementation.user import UserRepository as LayerRepository
from app.account.infrastructure.service.routes.user import ServiceUser as LayerService

def setup_user(api_server: FastAPI):
    print("setup >>> user")
    repo = LayerRepository()
    app = LayerApplication(repo)
    LayerService(api_server, app)