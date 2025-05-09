from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.config.db import BaseModel
from app.person.domain.enum.answer import EAnswerGeneral, EAnswerMigrant

from ..schema import SchemaPerson

class SocioculturalIdentity(BaseModel):
    __tablename__ = SchemaPerson('sociocultural_identity')

    id = Column(Integer, primary_key=True)
    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    person = relationship("Person", back_populates="sociocultural_identity")
    
    self_considers_indigenous = Column(Enum(EAnswerGeneral), nullable=False)
    key_indigenous_language = Column(String, nullable=True)
    self_considers_migrant = Column(Enum(EAnswerMigrant), nullable=False)
    key_country_origin = Column(String, nullable=True)
    key_religion = Column(String, nullable=True)
