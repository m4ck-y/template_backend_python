from app.health_monitoring.infrastructure.database.model.measure_type_group import MeasureTypeGroup as Table
from app.utils.infrastructure.database.implementation import BaseRepository
from app.health_monitoring.domain.schemas.measure_type_group import (
    SchemaMeasureTypeGroup as E,
    SchemaCreateMeasureTypeGroup as C,
    SchemaUpdateMeasureTypeGroup as U,
)

class MeasureTypeGroupRepository(BaseRepository[Table, C, U, E]):

    def __init__(self):
        super().__init__(Table, C, U, E)