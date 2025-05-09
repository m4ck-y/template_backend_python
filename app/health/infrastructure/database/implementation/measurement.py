from typing import Optional, List
from sqlalchemy.orm import Session
from app.config.db import datetime_now
from app.health.domain.repository.measurement import IRepositoryMeasurement as IRepository
from app.health.infrastructure.database.model.measurement import Measurement as Table
from app.health.domain.schemas.measurement import (
    SchemaMeasurement as E,
    SchemaCreateMeasurement as C,
    SchemaUpdateMeasurement as U,
)

class MeasurementGroupRepository(IRepository):

    def Create(self, entity: C, db: Session) -> int:
        new_entity = Table(**entity.model_dump())
        db.add(new_entity)
        db.commit()
        db.refresh(new_entity)
        return new_entity.id

    def Get(self, id: int, db: Session) -> Optional[E]:
        record = db.query(Table).filter(Table.id == id, Table.deleted_at.is_(None)).first()
        if record:
            return E.model_validate(record)
        return None

    def List(self, db: Session) -> List[E]:
        records = db.query(Table).filter(Table.deleted_at.is_(None)).all()
        return [E.model_validate(unit) for unit in records]

    def Update(self, value: U, db: Session) -> bool:
        record = db.query(Table).filter(Table.id == value.id, Table.deleted_at.is_(None)).first()
        if not record:
            return False
        for k, v in value.model_dump(exclude_unset=True).items():
            setattr(record, k, v)
        db.commit()
        db.refresh(record)
        return True

    def Delete(self, id: int, db: Session) -> bool:
        record = db.query(Table).filter(Table.id == id, Table.deleted_at.is_(None)).first()
        if not record:
            return False
        record.deleted_at = datetime_now()#db.delete(record)
        db.commit()
        return True