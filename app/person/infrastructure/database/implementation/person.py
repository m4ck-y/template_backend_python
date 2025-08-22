from app.person.infrastructure.database.model.person import Person as Table
from app.utils.infrastructure.database.implementation import BaseRepository
#from app.person.domain.repository.person import IRepositoryPerson
from app.person.domain.schemas.person import (
    SchemaCreateAPIPerson as C,
    SchemaItemPerson as I,
    SchemaDetailPerson as E,
    SchemaPersonUpdate as U,
)
class PersonRepository(BaseRepository[Table, C, I, E, U]):

    def __init__(self):
        super().__init__(Table, C, I, E, U)