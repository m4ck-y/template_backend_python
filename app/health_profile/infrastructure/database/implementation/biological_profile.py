from app.health_profile.infrastructure.database.model.biological_profile import BiologicalProfile as Table
from app.utils.infrastructure.database.base_implementation import BaseRepository
from app.health_profile.domain.schemas.biological_profile import (
    SchemaBiologicalProfile as E,
    SchemaCreateBiologicalProfile as C,
    SchemaUpdateBiologicalProfile as U,
)

class BiologicalProfileRepository(BaseRepository[Table, C, U, E]):

    def __init__(self):
        super().__init__(Table, C, U, E)