from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.models.base_model import BaseModel
from app.person.infrastructure.database.schema import PersonSchema


print(f"""

__tablename: {PersonSchema.TBL_BIRTH.name}
__table_args: {PersonSchema.NAME}
ForeignKey: {PersonSchema.TBL_PERSON.identifier}.id

""")

class Birth(BaseModel):
    __tablename__ = PersonSchema.TBL_BIRTH.name

    __table_args__ = {'schema': PersonSchema.TBL_BIRTH.schema}

    id_person = Column(Integer, ForeignKey(f"{PersonSchema.TBL_PERSON.identifier}.id"), nullable=False, unique=True)
    # 1:1 | 1 birth -> 1 person
    person = relationship("Person", back_populates="birth")
    key_birth_country = Column(String, nullable=False)
    key_state_birth = Column(String, nullable=False)
    birth_date = Column(DateTime(timezone=True), nullable=False)
    birth_date_timezone = Column(String, nullable=True)
