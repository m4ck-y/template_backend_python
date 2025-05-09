from abc import ABC, abstractmethod
from typing import List, Optional

from app.utils.domain.repository.base import TSession  # Tipado para la sesión de base de datos
from app.health.domain.schemas.measure_type import (
    SchemaMeasureType as E,
    SchemaCreateMeasureType as C,
    SchemaUpdateMeasureType as U,
)

class IRepositoryMeasureType(ABC):
    @abstractmethod
    def Create(self, value: C, session: TSession) -> int:
        raise NotImplementedError

    @abstractmethod
    def Get(self, id: int, session: TSession) -> Optional[E]:
        raise NotImplementedError

    @abstractmethod
    def List(self, session: TSession) -> List[E]:
        raise NotImplementedError

    @abstractmethod
    def Update(self, value: U, session: TSession) -> bool:
        raise NotImplementedError

    @abstractmethod
    def Delete(self, id: int, session: TSession) -> bool:
        raise NotImplementedError