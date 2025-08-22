from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.models.base_model import BaseModel
from app.person.infrastructure.database.schema import PersonSchema
from app.person.domain.enum.civil_status import ECivilStatus
from app.person.domain.enum.curp_sex import CURPSex

class LegalInfo(BaseModel):
    __tablename__ = PersonSchema.TBL_LEGAL_INFO.name

    __table_args__ = {'schema': PersonSchema.TBL_LEGAL_INFO.schema}

    id_person = Column(Integer, ForeignKey(f'{PersonSchema.TBL_PERSON.identifier}.id'), nullable=False)
    # 1:1 | 1 legal_info -> 1 person
    person = relationship("Person", back_populates="legal_info")

    type_national_id_sex = Column(Enum(CURPSex), nullable=False)
    type_civil_status = Column(Enum(ECivilStatus), nullable=False)
    key_nationality = Column(String, nullable=False)
