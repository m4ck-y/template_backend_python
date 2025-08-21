from app.health_monitoring.infrastructure.database.model.unit import Unit as Table
from app.utils.infrastructure.database.implementation import BaseRepository
from app.health_monitoring.domain.repository.unit import IRepositoryUnit
from app.health_monitoring.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaCreateUnit as C,
    SchemaUpdateUnit as U,
)

class UnitRepository(BaseRepository[Table, C, U, E]):

    def __init__(self):
        super().__init__(Table, C, U, E)