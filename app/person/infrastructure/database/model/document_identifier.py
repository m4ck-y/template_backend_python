from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.person.infrastructure.database.schema import PersonSchema

class DocumentIdentifier(BaseModel):

    __tablename__ = PersonSchema.TBL_DOCUMENT_IDENTIFIER.name

    __table_args__ = {'schema': PersonSchema.TBL_DOCUMENT_IDENTIFIER.schema}

    id_person_identifier = Column(Integer, ForeignKey(f'{PersonSchema.TBL_PERSON_IDENTIFIER.identifier}.id'), nullable=False)
    person_identifier = relationship("PersonIdentifier", back_populates="document_identifier")

    id_document = Column(Integer, ForeignKey(f'{PersonSchema.TBL_DOCUMENT.identifier}.id'), nullable=False)
    document = relationship("Document", back_populates="document_identifier")