from typing import Optional, List
from sqlalchemy.orm import Session
from app.config.db import datetime_now
from app.health.domain.repository.measure_group import IRepositoryMeasureGroup as IRepository
from app.health.infrastructure.database.model.measure_group import MeasureGroup as Table
from app.health.domain.schemas.measure_group import (
    SchemaMeasureGroup as E,
    SchemaCreateMeasureGroup as C,
    SchemaUpdateMeasureGroup as U,
)

class MeasureGroupRepository(IRepository):

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