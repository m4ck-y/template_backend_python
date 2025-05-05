from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base
from app.person.infrastructure.database.base import SchemaPerson

class DocumentType(Base):
    __tablename__ = SchemaPerson('document_type')

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    id_category = Column(Integer, ForeignKey(f'{SchemaPerson("document_category")}.id'), nullable=False)
    # 1 document_type -> 1 category
    category = relationship("DocumentCategory", back_populates="list_document_types")

    # 1:N | 1 document_type -> N documents     
    list_documents = relationship("Document", back_populates="document_type")