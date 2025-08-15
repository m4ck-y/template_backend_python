from fastapi import FastAPI
#from app.health.infrastructure.service.setup import setup_all as setup_health
from app.person.infrastructure.service.setup import setup_module_person


def init_api(api_server: FastAPI):
    print("init >>> api")
    #setup_health(api_server)
    #setup_module_person(api_server)