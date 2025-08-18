from fastapi import FastAPI
from app.health.infrastructure.service.setup.unit import setup as setup_unit
from app.health.infrastructure.service.setup.measurement import setup as setup_measurement
from app.health.infrastructure.service.setup.health_info import setup as setup_health
from app.health.infrastructure.service.setup.measure_group import setup as setup_measure_group
from app.health.infrastructure.service.setup.measure_type import setup as setup_measure_type
from app.health.infrastructure.service.setup.measure_type_group import setup as setup_measure_type_group


def setup_all(api_server: FastAPI):
    setup_measure_group(api_server)
    setup_unit(api_server)
    setup_measure_type(api_server)# id_unit
    setup_measure_type_group(api_server) # id_measure_type, id_measure_group
    setup_measurement(api_server) # id_measure_type, id_person
    setup_health(api_server) # id_person