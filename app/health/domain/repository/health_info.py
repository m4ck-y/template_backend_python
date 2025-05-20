from abc import ABC
from app.utils.domain.repository.base_repository import IBaseRepository
from app.health.domain.schemas.health_info import (
    SchemaHealthInfo as E,
    SchemaCreateHealthInfo as C,
    SchemaUpdateHealthInfo as U,
)

class IRepositoryHealthInfo(IBaseRepository[E, C, U], ABC):
    pass