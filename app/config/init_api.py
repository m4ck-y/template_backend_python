from fastapi import FastAPI
#from app.health.infrastructure.service.setup import setup_all as setup_health
from app.person.infrastructure.service.setup import setup_module_person
from app.account.infrastructure.service.setup import setup_module_account


def init_api(api_server: FastAPI):
    print("init >>> api")
    #setup_health(api_server)
    setup_module_person(api_server)
    setup_module_account(api_server)