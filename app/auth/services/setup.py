from fastapi import FastAPI
from .routes import ServiceAuth
from app.auth.application.auth import AuthApplication
from app.account.domain.repository.user import IRepositoryUser

def setup_auth(api_server: FastAPI, user_repo: IRepositoryUser):
    print("setup >>> auth")
    app = AuthApplication(user_repo=user_repo)
    ServiceAuth(api_server, app)


