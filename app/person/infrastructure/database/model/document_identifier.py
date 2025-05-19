from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.person.infrastructure.database.schema import SchemaPerson

class DocumentIdentifier(BaseModel):

    __tablename__ = SchemaPerson('document_identifier')

    id_person_identifier = Column(Integer, ForeignKey(f'{SchemaPerson("person_identifier")}.id'), nullable=False)
    person_identifier = relationship("PersonIdentifier", back_populates="document_identifier")
    
    id_document = Column(Integer, ForeignKey(f'{SchemaPerson("document")}.id'), nullable=False)
    document = relationship("Document", back_populates="document_identifier")