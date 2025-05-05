from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.config.db import Base
from app.person.domain.enum.identifier import EIdentifierType
from app.person.infrastructure.database.base import SchemaPerson

class IdentifierType(Base):
    __tablename__ = SchemaPerson('identifier_type')

    id = Column(Integer, primary_key=True)
    type_identifier = Column(Enum(EIdentifierType), nullable=False)
    name = Column(String, nullable=False)
    abbreviation = Column(String, nullable=False)
    country_code = Column(String, nullable=False)

    list_person_identifiers = relationship("PersonIdentifier", back_populates="identifier_type")