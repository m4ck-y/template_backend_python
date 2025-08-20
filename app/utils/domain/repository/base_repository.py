from abc import ABC, abstractmethod
from typing import Generic, List, Optional

from app.utils.domain.repository.base_session import TSession  # Solo se usa como tipado
from app.utils.domain.schemas.types import TSchemaItem, TSchemaDetail, TSchemaUpdate, TSchemaCreateAPI


class IBaseRepository(ABC, Generic[TSchemaCreateAPI, TSchemaItem, TSchemaDetail, TSchemaUpdate]):
    """
    Interfaz genérica de repositorio para operaciones CRUD sobre cualquier entidad del dominio.

    **Parámetros genéricos:**
    - `TSchemaCreateAPI`: Esquema de creación desde la API (ejemplo: `UserCreateAPI`)
    - `TSchemaItem`: Esquema simplificado para listados (ejemplo: `UserListItem`)
    - `TSchemaDetail`: Esquema detallado de retorno (ejemplo: `UserDetail`)
    - `TSchemaUpdate`: Esquema de actualización (ejemplo: `UserUpdate`)

    Esta interfaz define los contratos base que deben implementar los repositorios específicos
    para manejar operaciones de persistencia de datos. Está diseñada para mantener aislada 
    la lógica de dominio de la tecnología de persistencia (ORM, base de datos, etc.).
    """

    @abstractmethod
    def Create(self, value: TSchemaCreateAPI, session: TSession, auto_commit: bool = True) -> int:
        """
        Crea una nueva entidad en la base de datos.

        Args:
            value (TSchemaCreateAPI): Esquema con los datos necesarios para crear la entidad.
            session (TSession): Sesión activa de la base de datos.
            auto_commit (bool): Si se debe hacer commit automáticamente.

        Returns:
            int: ID de la entidad recién creada.
        """
        raise NotImplementedError

    @abstractmethod
    def List(self, session: TSession) -> List[TSchemaItem]:
        """
        Lista todas las entidades disponibles en formato resumido.

        Args:
            session (TSession): Sesión activa de la base de datos.

        Returns:
            List[TSchemaItem]: Lista de entidades representadas como ítems resumidos.
        """
        raise NotImplementedError

    @abstractmethod
    def Get(self, id: int, session: TSession) -> Optional[TSchemaDetail]:
        """
        Recupera una entidad por su ID.

        Args:
            id (int): Identificador único.
            session (TSession): Sesión activa de la base de datos.

        Returns:
            Optional[TSchemaDetail]: Detalle de la entidad o `None` si no existe.
        """
        raise NotImplementedError

    @abstractmethod
    def Update(self, value: TSchemaUpdate, session: TSession, auto_commit: bool = True) -> bool:
        """
        Actualiza una entidad existente.

        Args:
            value (TSchemaUpdate): Esquema con los campos a modificar.
            session (TSession): Sesión activa.
            auto_commit (bool): Si se debe hacer commit automáticamente.

        Returns:
            bool: `True` si la actualización fue exitosa, `False` en caso contrario.
        """
        raise NotImplementedError

    @abstractmethod
    def Delete(self, id: int, session: TSession, auto_commit: bool = True) -> bool:
        """
        Elimina una entidad por ID.

        Args:
            id (int): ID de la entidad.
            session (TSession): Sesión activa.
            auto_commit (bool): Si se debe hacer commit automáticamente.

        Returns:
            bool: `True` si la eliminación fue exitosa, `False` si no se encontró la entidad.
        """
        raise NotImplementedError