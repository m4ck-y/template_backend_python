from abc import ABC
from app.utils.domain.repository.base_repository import IBaseRepository
from app.health_profile.domain.schemas.biological_profile import (
    SchemaBiologicalProfile as E,
    SchemaCreateBiologicalProfile as C,
    SchemaUpdateBiologicalProfile as U,
)

class IRepositoryBiologicalProfile(IBaseRepository[E, C, U], ABC):
    pass