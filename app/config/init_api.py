from fastapi import FastAPI
#from app.health.infrastructure.service.setup import setup_all as setup_health
from app.auth.services.setup import setup_auth
from app.person.infrastructure.service.setup import setup_module_person
from app.account.infrastructure.service.setup import setup_module_account


def init_api(api_server: FastAPI):
    print("init >>> api")
    #setup_health(api_server)
    setup_module_person(api_server)
    repo_user = setup_module_account(api_server)
    setup_auth(api_server, repo_user)