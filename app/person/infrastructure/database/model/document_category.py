from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.person.infrastructure.database.schema import SchemaPerson

class DocumentCategory(BaseModel):

    __tablename__ = SchemaPerson('document_category')

    name = Column(String, nullable=False)

    # 1:N | 1 document_type -> 1 document_category
    list_document_types = relationship("DocumentType", back_populates="category")