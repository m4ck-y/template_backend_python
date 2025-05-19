from app.health.infrastructure.database.model.unit import Unit as Table
from app.utils.infrastructure.database.base_implementation import BaseRepository
from app.health.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaCreateUnit as C,
    SchemaUpdateUnit as U,
)

class UnitRepository(BaseRepository[Table, C, U, E]):

    def __init__(self):
        super().__init__(Table, C, U, E)