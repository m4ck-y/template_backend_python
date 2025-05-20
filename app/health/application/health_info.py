from app.utils.application.base import BaseLayerApplication
from app.health.domain.repository.health_info import IRepositoryHealthInfo as IRepository
from app.health.domain.schemas.measurement import (
    SchemaMeasurement as E,
    SchemaCreateMeasurement as C,
    SchemaUpdateMeasurement as U,
)

class HealthInfoApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IRepository):
        super().__init__(repository)