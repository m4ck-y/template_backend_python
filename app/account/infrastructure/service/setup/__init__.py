from fastapi import FastAPI
from app.account.infrastructure.service.setup.user import setup_user

def setup_module_account(api_server: FastAPI):
    setup_user(api_server)