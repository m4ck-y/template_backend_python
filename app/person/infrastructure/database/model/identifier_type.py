from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.person.domain.enum.identifier import EIdentifierType
from app.person.infrastructure.database.schema import PersonSchema

class IdentifierType(BaseModel):
    __tablename__ = PersonSchema.TBL_IDENTIFIER_TYPE.name

    __table_args__ = {'schema': PersonSchema.TBL_IDENTIFIER_TYPE.schema}

    type_identifier = Column(Enum(EIdentifierType), nullable=False)
    name = Column(String, nullable=False)
    abbreviation = Column(String, nullable=False)
    country_code = Column(String, nullable=False)

    list_person_identifiers = relationship("PersonIdentifier", back_populates="identifier_type")