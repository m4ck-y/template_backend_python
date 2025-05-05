from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.db import Base
from app.person.infrastructure.database.base import SchemaPerson

class DocumentCategory(Base):

    __tablename__ = SchemaPerson('document_category')

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # 1:N | 1 document_type -> 1 document_category
    list_document_types = relationship("DocumentType", back_populates="category")