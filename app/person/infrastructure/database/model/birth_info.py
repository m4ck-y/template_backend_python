from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.person.infrastructure.database.schema import PersonSchema


print(f"""

__tablename: {PersonSchema.TBL_BIRTH_INFO.name}
__table_args: {PersonSchema.NAME}
ForeignKey: {PersonSchema.TBL_PERSON.identifier}.id

""")

class BirthInfo(BaseModel):
    __tablename__ = PersonSchema.TBL_BIRTH_INFO.name

    __table_args__ = {'schema': PersonSchema.TBL_BIRTH_INFO.schema}

    id_person = Column(Integer, ForeignKey(f"{PersonSchema.TBL_PERSON.identifier}.id"), nullable=False, unique=True)
    # 1:1 | 1 birth_info -> 1 person
    person = relationship("Person", back_populates="birth_info")
    key_birth_country = Column(String, nullable=False)
    key_state_birth = Column(String, nullable=False)
    birth_date = Column(DateTime(timezone=True), nullable=False)
    birth_date_timezone = Column(String, nullable=True)
