from sqlalchemy import Column, Integer, String, DateTime, Enum, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel

from ..schema import SchemaPerson

class BirthInfo(BaseModel):
    __tablename__ = SchemaPerson('birth_info')

    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    key_birth_country = Column(String, nullable=False)
    key_state_birth = Column(String, nullable=False)
    birth_date = Column(DATETIME, nullable=False)
    birth_date_timezone = Column(String, nullable=True)

    person = relationship("Person", back_populates="birth_info")