from typing import List
from app.utils.domain.repository.base import TSession
from app.health.domain.repository.measure_type import IRepositoryMeasureType as IRepository
from app.health.domain.schemas.measure_type import (
    SchemaMeasureType as E,
    SchemaCreateMeasureType as C,
    SchemaUpdateMeasureType as U,
)

class MeasureTypeApplication:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def Create(self, value: C, db: TSession) -> E:
        return self.repository.Create(value, db)

    def Get(self, id: int, db: TSession) -> E | None:
        return self.repository.Get(id, db)

    def List(self, db: TSession) -> List[E]:
        return self.repository.List(db)

    def Update(self, entity: U, db: TSession) -> bool:
        return self.repository.Update(entity, db)

    def Delete(self, id: int, db: TSession) -> bool:
        return self.repository.Delete(id, db)
