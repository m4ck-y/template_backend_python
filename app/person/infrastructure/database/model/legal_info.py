from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.config.db import Base
from app.person.infrastructure.database.base import SchemaPerson
from app.person.domain.enum.civil_status import ECivilStatus
from app.person.domain.enum.curp_sex import CURPSex

class LegalInfo(Base):
    __tablename__ = SchemaPerson('legal_info')

    id = Column(Integer, primary_key=True)
    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    type_national_id_sex = Column(Enum(CURPSex), nullable=False)
    type_civil_status = Column(Enum(ECivilStatus), nullable=False)
    key_nationality = Column(String, nullable=False)

    person = relationship("Person", back_populates="legal_info")