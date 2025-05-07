from typing import Optional, List
from sqlalchemy.orm import Session
from app.health.domain.repository.unit import IRepositoryUnit
from app.health.infrastructure.database.model.unit import Unit as Table
from app.health.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaUnitCreate as C,
    SchemaUnitUpdate as U,
)

class UnitRepository(IRepositoryUnit):

    def Create(self, entity: C, db: Session) -> int:
        new_unit = Table(**entity.model_dump())
        db.add(new_unit)
        db.commit()
        db.refresh(new_unit)
        return new_unit.id

    def Get(self, id: int, db: Session) -> Optional[E]:
        unit = db.query(Table).filter(Table.id == id).first()
        if unit:
            return E.model_validate(unit)
        return None

    def List(self, db: Session) -> List[E]:
        units = db.query(Table).all()
        print(units[0])
        return [E.model_validate(unit) for unit in units]

    def Update(self, value: U, db: Session) -> bool:
        unit = db.query(Table).filter(Table.id == value.id).first()
        if not unit:
            return False
        for k, v in value.model_dump(exclude_unset=True).items():
            setattr(unit, k, v)
        db.commit()
        db.refresh(unit)
        return True

    def Delete(self, id: int, db: Session) -> bool:
        unit = db.query(Table).filter(Table.id == id).first()
        if not unit:
            return False
        db.delete(unit)
        db.commit()
        return True
