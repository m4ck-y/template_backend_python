from fastapi import FastAPI
from app.health.infrastructure.service.setup import setup_all


def init_api(api_server: FastAPI):
    print("init >>> api")
    setup_all(api_server)