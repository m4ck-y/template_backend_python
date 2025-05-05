from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base
from app.person.infrastructure.database.base import SchemaPerson

class PersonIdentifier(Base):

    __tablename__ = SchemaPerson('person_identifier')

    id = Column(Integer, primary_key=True)

    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    # 1 person_identifier -> 1 person
    person = relationship("Person", back_populates="list_person_identifiers")

    id_identifier_type = Column(Integer, ForeignKey(f'{SchemaPerson("identifier_type")}.id'), nullable=False)
    # 1 person_identifier -> 1 identifier_type
    identifier_type = relationship("IdentifierType", back_populates="list_person_identifiers")

    identifier_value = Column(String, nullable=False)
