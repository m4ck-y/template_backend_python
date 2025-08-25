from app.utils.application.base import BaseLayerApplication
from app.utils.domain.repository.base_repository import IBaseRepository
from app.account.domain.schemas.user import (
    SchemaCreateAPIUser as C,
    SchemaItemUser as I,
    SchemaDetailUser as E,
    SchemaUserUpdate as U
)

class UserApplication(BaseLayerApplication[C, I, E, U]):
    def __init__(self, repository: IBaseRepository[C, I, E, U]):
        super().__init__(repository)