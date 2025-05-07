from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional
from app.utils.domain.repository.base import Session  # Solo se usa como tipado

# Tipos genéricos para la entidad principal y sus esquemas de creación y actualización
E = TypeVar('SchemaEntity')         # Ejemplo: CountryFlag
C = TypeVar('SchemaEntityCreate')   # Ejemplo: CountryFlagCreate
U = TypeVar('SchemaEntityUpdate')   # Ejemplo: CountryFlagUpdate

class IRepository(ABC, Generic[E, C, U]):
    """
    Interfaz genérica de repositorio para operaciones CRUD sobre cualquier entidad del dominio.

    Esta interfaz define los contratos base que deben implementar los repositorios específicos
    para manejar operaciones de persistencia de datos. Está diseñada para mantener aislada 
    la lógica de dominio de la tecnología de persistencia (ORM, base de datos, etc.).

    Notas:
    - La gestión de sesiones y transacciones corresponde exclusivamente a la capa de infraestructura.
    - Los errores relacionados a la base de datos (como fallas de conexión) deben capturarse en capas externas.
    - Esta clase no debe incluir lógica HTTP ni depender de FastAPI u otros frameworks externos.
    """

    @abstractmethod
    def Create(self, value: C, session: Session) -> int:
        """
        Crea una nueva entidad en la base de datos.

        Args:
            value (C): Esquema de creación de la entidad.
            session (Session): Sesión activa de base de datos.

        Returns:
            int: ID de la entidad recién creada.
        """
        raise NotImplementedError

    @abstractmethod
    def Get(self, id: int, session: Session) -> Optional[E]:
        """
        Recupera una entidad por su ID.

        Args:
            id (int): Identificador único de la entidad.
            session (Session): Sesión activa de base de datos.

        Returns:
            Optional[E]: Entidad encontrada o None si no existe.
        """
        raise NotImplementedError

    @abstractmethod
    def List(self, session: Session) -> List[E]:
        """
        Lista todas las entidades disponibles en la base de datos.

        Args:
            session (Session): Sesión activa de base de datos.

        Returns:
            List[E]: Lista completa de entidades.
        """
        raise NotImplementedError

    @abstractmethod
    def Update(self, value: U, session: Session) -> bool:
        """
        Actualiza una entidad existente.

        Args:
            value (U): Esquema con los campos a actualizar.
            session (Session): Sesión activa de base de datos.

        Returns:
            bool: True si la actualización fue exitosa, False si la entidad no fue encontrada.
        """
        raise NotImplementedError

    @abstractmethod
    def Delete(self, id: int, session: Session) -> bool:
        """
        Elimina una entidad por su ID.

        Args:
            id (int): Identificador único de la entidad a eliminar.
            session (Session): Sesión activa de base de datos.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encontró la entidad.
        """
        raise NotImplementedError