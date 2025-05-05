from sqlalchemy import Column, Integer, String, DateTime, Enum, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base

from ..base import SchemaPerson

class BirthInfo(Base):
    __tablename__ = SchemaPerson('birth_info')

    id = Column(Integer, primary_key=True)
    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    key_birth_country = Column(String, nullable=False)
    key_state_birth = Column(String, nullable=False)
    birth_date = Column(DATETIME, nullable=False)
    birth_date_timezone = Column(String, nullable=True)

    person = relationship("Person", back_populates="birth_info")