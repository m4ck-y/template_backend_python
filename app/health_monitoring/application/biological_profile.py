from app.utils.application.base import BaseLayerApplication
from app.health_monitoring.domain.repository.biological_profile import IRepositoryHealthInfo as IRepository
from app.health_monitoring.domain.schemas.measurement import (
    SchemaMeasurement as E,
    SchemaCreateMeasurement as C,
    SchemaUpdateMeasurement as U,
)

class BiologicalProfileApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IRepository):
        super().__init__(repository)