from app.health.infrastructure.database.model.measure_group import MeasureGroup as Table
from app.utils.infrastructure.database.base_implementation import BaseRepository
from app.health.domain.schemas.measure_group import (
    SchemaMeasureGroup as E,
    SchemaCreateMeasureGroup as C,
    SchemaUpdateMeasureGroup as U,
)

class MeasureGroupRepository(BaseRepository[Table, C, U, E]):
    def __init__(self):
        super().__init__(Table, C, U, E)