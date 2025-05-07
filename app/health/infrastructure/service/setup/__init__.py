from fastapi import FastAPI
from app.health.infrastructure.service.setup.unit import setup as setup_unit


def setup_all(api_server: FastAPI):
    setup_unit(api_server)