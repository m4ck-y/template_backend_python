from fastapi import FastAPI
from app.account.infrastructure.service.setup.user import setup_user
from app.account.domain.repository.user import IRepositoryUser

ROUTE_NAME = "account"

def setup_module_account(api_server: FastAPI) -> IRepositoryUser:
    return setup_user(api_server, parent_path=ROUTE_NAME)