from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.config.db import Base
from app.person.infrastructure.database.base import SchemaPerson

class Document(Base):

    __tablename__ = SchemaPerson('document')

    id = Column(Integer, primary_key=True)

    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    # 1 document -> 1 person
    person = relationship("Person", back_populates="list_documents")

    url_file = Column(String, nullable=False)
    url_thumbnail = Column(String)
    title = Column(String, nullable=False)
    description = Column(String)

    id_document_type = Column(Integer, ForeignKey(f'{SchemaPerson("document_type")}.id'), nullable=False)
    # 1 document -> 1 document_type
    document_type = relationship("DocumentType", back_populates="list_documents")

    issued_at = Column(Date, nullable=False)
    expires_at = Column(Date, nullable=False)
    verification_status = Column(String, nullable=False)
    verified_by = Column(String, nullable=False)