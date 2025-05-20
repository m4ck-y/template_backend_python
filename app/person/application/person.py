from app.utils.application.base import BaseLayerApplication
from app.utils.domain.repository.base_repository import IBaseRepository
from app.person.domain.schemas.person import (
    SchemaPerson as E,
    SchemaPersonCreate as C,
    SchemaPersonUpdate as U,
)
class PersonApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IBaseRepository[E, C, U]):
        super().__init__(repository)