from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.models.base_model import BaseModel
from app.person.infrastructure.database.schema import PersonSchema

class Document(BaseModel):

    __tablename__ = PersonSchema.TBL_DOCUMENT.name

    __table_args__ = {'schema': PersonSchema.TBL_DOCUMENT.schema}

    id_person = Column(Integer, ForeignKey(f'{PersonSchema.TBL_PERSON.identifier}.id'), nullable=False)
    # 1:1 | 1 document -> 1 person
    person = relationship("Person", back_populates="list_documents")

    url_file = Column(String, nullable=False)
    url_thumbnail = Column(String)
    title = Column(String, nullable=False)
    description = Column(String)

    id_document_type = Column(Integer, ForeignKey(f'{PersonSchema.TBL_DOCUMENT_TYPE.identifier}.id'), nullable=False)
    # 1:1 | 1 document -> 1 document_type
    document_type = relationship("DocumentType", back_populates="list_documents")

    issued_at = Column(Date, nullable=False)
    expires_at = Column(Date, nullable=False)
    verification_status = Column(String, nullable=False)
    verified_by = Column(String, nullable=False)

    # RELATIONSHIPS
    # 1:1 | 1 document -> 1 document_identifier
    document_identifier = relationship("DocumentIdentifier", back_populates="document")