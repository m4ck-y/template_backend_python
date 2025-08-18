from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.person.infrastructure.database.schema import PersonSchema

class PersonIdentifier(BaseModel):

    __tablename__ = PersonSchema.TBL_PERSON_IDENTIFIER.name

    __table_args__ = {'schema': PersonSchema.TBL_PERSON_IDENTIFIER.schema}

    id_person = Column(Integer, ForeignKey(f'{PersonSchema.TBL_PERSON.identifier}.id'), nullable=False)
    # 1 person_identifier -> 1 person
    person = relationship("Person", back_populates="list_person_identifiers")

    id_identifier_type = Column(Integer, ForeignKey(f'{PersonSchema.TBL_IDENTIFIER_TYPE.identifier}.id'), nullable=False)
    # 1 person_identifier -> 1 identifier_type
    identifier_type = relationship("IdentifierType", back_populates="list_person_identifiers", uselist=False)

    identifier_value = Column(String, nullable=False)

    #RELATIONSHIPS
    # 1:1 | 1 person_identifier -> 1 document_identifier
    document_identifier = relationship("DocumentIdentifier", back_populates="person_identifier")
