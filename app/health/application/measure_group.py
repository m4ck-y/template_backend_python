from app.utils.application.base import BaseLayerApplication
from app.health.domain.repository.measure_group import IRepositoryMeasureGroup as IRepository
from app.health.domain.schemas.measure_group import (
    SchemaMeasureGroup as E,
    SchemaCreateMeasureGroup as C,
    SchemaUpdateMeasureGroup as U,
)

class MeasureGroupApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IRepository):
        super().__init__(repository)