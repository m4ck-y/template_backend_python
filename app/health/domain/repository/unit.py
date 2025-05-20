from abc import ABC, abstractmethod
from typing import List

from app.utils.domain.repository.base_session import TSession  # Tipado para la sesión de base de datos
from app.health.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaCreateUnit as C,
    SchemaUpdateUnit as U,
)
from app.utils.domain.repository.base_repository import IBaseRepository

class IRepositoryUnit(IBaseRepository[E, C, U], ABC):
    @abstractmethod
    def FindByName(self, name: str, session: TSession) -> List[E]:
        """
        Custom method to find Units by their name.

        Args:
            name (str): Name of the unit (e.g., 'Kilogram', 'Meter').
            session (TSession): Active database session.

        Returns:
            List[SchemaUnit]: List of units matching the given name.
        """
        raise NotImplementedError