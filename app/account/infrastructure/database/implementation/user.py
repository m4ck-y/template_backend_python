from app.account.infrastructure.database.model.user import User as Table
from sqlalchemy import and_
from app.utils.infrastructure.database.implementation import BaseRepository
from app.account.domain.schemas.user import (
    SchemaCreateAPIUser as C,
    SchemaItemUser as I,
    SchemaDetailUser as E,
    SchemaUserUpdate as U,
    SchemaDetailUserWithPassword,
)

class UserRepository(BaseRepository[C, I, E, U, Table]):
    def __init__(self):
        super().__init__(Table, C, I, E, U)

    def GetWithPassword(self, username: str, db) -> SchemaDetailUserWithPassword | None:
        """Obtiene un usuario por su nombre de usuario, incluyendo la contraseña hasheada.
        Args:
            username (str): **Nombre de usuario** del usuario.
            db (TSession): **Sesión de base de datos**.
        Returns:
            SchemaUserWithPassword | None: **Esquema detallado del usuario** si se encuentra, None en caso contrario.
        """
        result = (
            db.query(Table)
            .filter(and_(Table.username == username, Table.deleted_at.is_(None)))
            .first()
        )
        if result:
            return SchemaDetailUserWithPassword.model_validate(result)