from abc import ABC
from app.utils.domain.repository.base_repository import IBaseRepository
from app.health.domain.schemas.measure_type import (
    SchemaListItemMeasureType as E,
    SchemaCreateMeasureType as C,
    SchemaUpdateMeasureType as U,
)

class IRepositoryMeasureType(IBaseRepository[E, C, U], ABC):
    pass