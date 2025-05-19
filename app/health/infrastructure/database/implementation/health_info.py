from app.health.infrastructure.database.model.health_info import HealthInfo as Table
from app.utils.infrastructure.database.base_implementation import BaseRepository
from app.health.domain.schemas.health_info import (
    SchemaHealthInfo as E,
    SchemaCreateHealthInfo as C,
    SchemaUpdateHealthInfo as U,
)

class HealthInfoRepository(BaseRepository[Table, C, U, E]):

    def __init__(self):
        super().__init__(Table, C, U, E)