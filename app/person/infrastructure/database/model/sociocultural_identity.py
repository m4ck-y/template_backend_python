from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from app.person.domain.enum.answer import EAnswerGeneral, EAnswerMigrant

from ..schema import PersonSchema

class SocioculturalIdentity(BaseModel):
    __tablename__ = PersonSchema.TBL_SOCIOCULTURAL_IDENTITY.name

    __table_args__ = {'schema': PersonSchema.TBL_SOCIOCULTURAL_IDENTITY.schema}

    id_person = Column(Integer, ForeignKey(f'{PersonSchema.TBL_PERSON.identifier}.id'), nullable=False)
    person = relationship("Person", back_populates="sociocultural_identity")
    
    self_considers_indigenous = Column(Enum(EAnswerGeneral), nullable=False)
    key_indigenous_language = Column(String, nullable=True)
    self_considers_migrant = Column(Enum(EAnswerMigrant), nullable=False)
    key_country_origin = Column(String, nullable=True)
    key_religion = Column(String, nullable=True)
