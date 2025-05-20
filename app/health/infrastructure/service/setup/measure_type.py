from fastapi import FastAPI
from app.utils.application.base import BaseLayerApplication as LayerApplication
from app.health.infrastructure.database.implementation.measure_type import MeasureTypeRepository as LayerRepository
from app.health.infrastructure.service.routes.measure_type import ServiceMeasureType as LayerService
from app.utils.enum.str_color import StrColor

str_color = StrColor()

def setup(api_server: FastAPI):
    print(str_color.BLUE("setup >>> measure_type <<<<<<"))
    repo = LayerRepository()
    print(str_color.BLUE("setup >>> measure_type >>> repo"), type(repo), repo)
    app = LayerApplication(repo)
    LayerService(api_server,app, "health")