from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.models.base_model import BaseModel
from app.person.infrastructure.database.schema import PersonSchema

print(f"""

__tablename: {PersonSchema.TBL_DOCUMENT_CATEGORY.name}
__table_args: {PersonSchema.NAME}

""")

class DocumentCategory(BaseModel):

    __tablename__ = PersonSchema.TBL_DOCUMENT_CATEGORY.name

    __table_args__ = {'schema': PersonSchema.TBL_DOCUMENT_CATEGORY.schema}

    name = Column(String, nullable=False)

    # 1:N | 1 document_type -> 1 document_category
    list_document_types = relationship("DocumentType", back_populates="category")