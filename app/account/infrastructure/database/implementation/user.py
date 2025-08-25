from app.account.infrastructure.database.model.user import User as Table
from app.utils.infrastructure.database.implementation import BaseRepository
from app.account.domain.schemas.user import (
    SchemaCreateAPIUser as C,
    SchemaItemUser as I,
    SchemaDetailUser as E,
    SchemaUserUpdate as U
)

class UserRepository(BaseRepository[C, I, E, U, Table]):
    def __init__(self):
        super().__init__(Table, C, I, E, U)