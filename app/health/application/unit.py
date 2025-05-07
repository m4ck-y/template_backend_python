from typing import List
from app.utils.domain.repository.base import TSession
from app.health.domain.repository.unit import IRepositoryUnit as IRepository
from app.health.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaUnitCreate as C,
    SchemaUnitUpdate as U,
)

class UnitApplication:
    """
    Application service layer for Unit entities.

    This class acts as an intermediary between the infrastructure (API, CLI, etc.)
    and the domain persistence logic. It contains no business logic; it simply
    delegates to the repository and coordinates flow.

    Dependencies:
    - IRepository: A repository implementing standard CRUD operations for Unit.
    - Session: Database session injected by the infrastructure layer (e.g., FastAPI dependency).
    """

    def __init__(self, repository: IRepository):
        self.repository = repository

    def Create(self, value: C, db: TSession) -> E:
        """
        Creates a new Unit of measurement.

        Args:
            value (SchemaUnitCreate): The data for the new Unit.
            db (Session): The active database session (injected via FastAPI).

        Returns:
            SchemaUnit: The newly created Unit with its assigned ID.
        """
        return self.repository.Create(value, db)

    def Get(self, id: int, db: TSession) -> E | None:
        """
        Retrieves a Unit by its ID.

        Args:
            id (int): The ID of the Unit to retrieve.
            db (Session): The active database session.

        Returns:
            SchemaUnit | None: The Unit if found, otherwise None.
        """
        return self.repository.Get(id, db)

    def List(self, db: TSession) -> List[E]:
        """
        Lists all Units stored in the system.

        Args:
            db (Session): The active database session.

        Returns:
            List[SchemaUnit]: A list of all registered Units.
        """
        return self.repository.List(db)

    def Update(self, entity: U, db: TSession) -> bool:
        """
        Updates an existing Unit.

        Args:
            entity (SchemaUnitUpdate): The updated data (must include the Unit ID).
            db (Session): The active database session.

        Returns:
            bool: True if the update was successful, False if the Unit was not found.
        """
        return self.repository.Update(entity, db)

    def Delete(self, id: int, db: TSession) -> bool:
        """
        Deletes a Unit by its ID.

        Args:
            id (int): The ID of the Unit to delete.
            db (Session): The active database session.

        Returns:
            bool: True if the deletion was successful, False if the Unit was not found.
        """
        return self.repository.Delete(id, db)
