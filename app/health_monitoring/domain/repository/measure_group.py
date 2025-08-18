from abc import ABC
from app.utils.domain.repository.base_repository import IBaseRepository
from app.health_monitoring.domain.schemas.measure_group import (
    SchemaMeasureGroup as E,
    SchemaCreateMeasureGroup as C,
    SchemaUpdateMeasureGroup as U,
)

class IRepositoryMeasureGroup(IBaseRepository[E, C, U], ABC):
    pass