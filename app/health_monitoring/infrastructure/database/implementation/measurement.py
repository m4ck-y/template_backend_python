from app.health_monitoring.infrastructure.database.model.measurement import Measurement as Table
from app.utils.infrastructure.database.implementation import BaseRepository
from app.health_monitoring.domain.schemas.measurement import (
    SchemaMeasurement as E,
    SchemaCreateMeasurement as C,
    SchemaUpdateMeasurement as U,
)

class MeasurementRepository(BaseRepository[Table, C, U, E]):

    def __init__(self):
        super().__init__(Table, C, U, E)