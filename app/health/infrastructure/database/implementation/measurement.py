from app.health.infrastructure.database.model.measurement import Measurement as Table
from app.utils.infrastructure.database.base_implementation import BaseRepository
from app.health.domain.schemas.measurement import (
    SchemaMeasurement as E,
    SchemaCreateMeasurement as C,
    SchemaUpdateMeasurement as U,
)

class MeasurementGroupRepository(BaseRepository[Table, C, U, E]):

    def __init__(self):
        super().__init__(Table, C, U, E)