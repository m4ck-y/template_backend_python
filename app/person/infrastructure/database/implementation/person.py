from app.person.infrastructure.database.model.person import Person as Table
from app.utils.infrastructure.database.implementation import BaseRepository
#from app.person.domain.repository.person import IRepositoryPerson
from app.person.domain.schemas.person import (
    SchemaPerson as E,
    SchemaPersonCreate as C,
    SchemaPersonUpdate as U,
)

class PersonRepository(BaseRepository[Table, C, U, E]):

    def __init__(self):
        super().__init__(Table, C, U, E)