from app.utils.application.base import BaseLayerApplication
from app.health_monitoring.domain.repository.measure_type_group import IRepositoryMeasureTypeGroup as IRepository
from app.health_monitoring.domain.schemas.measure_type_group import (
    SchemaMeasureTypeGroup as E,
    SchemaCreateMeasureTypeGroup as C,
    SchemaUpdateMeasureTypeGroup as U,
)

class MeasureTypeGroupApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IRepository):
        super().__init__(repository)