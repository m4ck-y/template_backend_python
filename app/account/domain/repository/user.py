from abc import ABC, abstractmethod
from app.utils.domain.repository.base_repository import IBaseRepository
from app.account.domain.schemas.user import (
    SchemaCreateAPIUser as C,
    SchemaItemUser as I,
    SchemaDetailUser as E,
    SchemaUserUpdate as U,
    SchemaDetailUserWithPassword,
)
from app.utils.domain.repository.base_session import TSession  # Solo se usa como tipado


class IRepositoryUser(IBaseRepository[C, I, E, U], ABC):
    @abstractmethod
    def GetWithPassword(self, username: str, db: TSession) -> SchemaDetailUserWithPassword | None:
        """Obtiene un usuario por su nombre de usuario, incluyendo la contraseña hasheada.

        Args:
            username (str): Nombre de usuario del usuario.
            db (TSession): Sesión de base de datos.

        Returns:
            SchemaUserWithPassword | None: Esquema del usuario (username, password) si se encuentra, None en caso contrario.
        """
        raise NotImplementedError