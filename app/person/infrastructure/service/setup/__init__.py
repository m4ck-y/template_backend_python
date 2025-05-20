from fastapi import FastAPI
from app.person.infrastructure.service.setup.person import setup_person


def setup_module_person(api_server: FastAPI):
    setup_person(api_server)