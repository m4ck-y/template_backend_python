from abc import ABC, abstractmethod
from typing import List, Optional

from app.utils.domain.repository.base import TSession  # Tipado para la sesión de base de datos
from app.health.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaUnitCreate as C,
    SchemaUnitUpdate as U,
)


class IRepositoryUnit(ABC):
    """
    Repository interface for managing Unit entities in the domain layer.

    This interface defines the standard CRUD operations that any persistence
    implementation must provide for the 'Unit' entity, which represents units of
    measurement such as 'Kilogram', 'Meter', etc.

    Notes:
    - Session and transaction control are managed at the infrastructure level.
    - Database-related exceptions (e.g., connection errors) must be handled outside of this interface.
    - This class should not include HTTP logic or dependencies on web frameworks like FastAPI.

    Related Entity: Unit of measurement (e.g., 'kg', 'L', '°C'), used in medical or scientific systems.
    """

    @abstractmethod
    def Create(self, value: C, session: TSession) -> int:
        """
        Creates a new Unit entity in the database.

        Args:
            value (SchemaUnitCreate): Data for the unit to be created.
            session (TSession): Active database session.

        Returns:
            int: ID of the newly created unit.

        Example (Spanish):
            Crear una unidad de medida como 'Litro' con símbolo 'L'.
        """
        raise NotImplementedError

    @abstractmethod
    def Get(self, id: int, session: TSession) -> Optional[E]:
        """
        Retrieves a Unit entity by its unique ID.

        Args:
            id (int): Unique identifier of the unit.
            session (TSession): Active database session.

        Returns:
            Optional[SchemaUnit]: The unit if found, otherwise None.

        Example (Spanish):
            Buscar la unidad con ID 5 para mostrar sus detalles.
        """
        raise NotImplementedError

    @abstractmethod
    def List(self, session: TSession) -> List[E]:
        """
        Returns a list of all Unit entities.

        Args:
            session (TSession): Active database session.

        Returns:
            List[SchemaUnit]: List of all units stored in the system.

        Example (Spanish):
            Listar todas las unidades disponibles: 'kg', 'm', 'L', etc.
        """
        raise NotImplementedError

    @abstractmethod
    def Update(self, value: U, session: TSession) -> bool:
        """
        Updates an existing Unit entity.

        Args:
            value (SchemaUnitUpdate): Object containing the fields to update.
            session (TSession): Active database session.

        Returns:
            bool: True if update was successful, False if the entity was not found.

        Example (Spanish):
            Actualizar el nombre de una unidad con ID 2 de 'litro' a 'Litro'.
        """
        raise NotImplementedError

    @abstractmethod
    def Delete(self, id: int, session: TSession) -> bool:
        """
        Deletes a Unit entity by its ID.

        Args:
            id (int): Unique identifier of the unit to delete.
            session (TSession): Active database session.

        Returns:
            bool: True if deletion was successful, False if the entity was not found.

        Example (Spanish):
            Eliminar la unidad con ID 7 si ya no se utiliza.
        """
        raise NotImplementedError
