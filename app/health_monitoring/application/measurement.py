from app.health_monitoring.domain.repository.measurement import IRepositoryMeasurement as IRepository
from app.utils.application.base import BaseLayerApplication
from app.health_monitoring.domain.schemas.measurement import (
    SchemaMeasurement as E,
    SchemaCreateMeasurement as C,
    SchemaUpdateMeasurement as U,
)

class MeasurementApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IRepository):
        super().__init__(repository)