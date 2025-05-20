from abc import ABC
from app.utils.domain.repository.base_repository import IBaseRepository
from app.health.domain.schemas.measure_type_group import (
    SchemaMeasureTypeGroup as E,
    SchemaCreateMeasureTypeGroup as C,
    SchemaUpdateMeasureTypeGroup as U,
)

class IRepositoryMeasureTypeGroup(IBaseRepository[E, C, U], ABC):
    pass