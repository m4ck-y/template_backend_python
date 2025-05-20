from abc import ABC
from app.utils.domain.repository.base_repository import IBaseRepository
from app.health.domain.schemas.measurement import (
    SchemaMeasurement as E,
    SchemaCreateMeasurement as C,
    SchemaUpdateMeasurement as U,
)

class IRepositoryMeasurement(IBaseRepository[E, C, U], ABC):
    pass