from app.utils.application.base import BaseLayerApplication
from app.utils.domain.repository.base_repository import IBaseRepository
from app.person.domain.schemas.person import (
    SchemaCreateAPIPerson as C,
    SchemaItemPerson as I,
    SchemaDetailPerson as E,
    SchemaPersonUpdate as U,
)
class PersonApplication(BaseLayerApplication[C, I, E, U]):
    def __init__(self, repository: IBaseRepository[C, I, E, U]):
        super().__init__(repository)