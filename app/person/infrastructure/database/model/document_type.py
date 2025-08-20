from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.models.base_model import BaseModel
from app.person.infrastructure.database.schema import PersonSchema

print(f"""

__tablename: {PersonSchema.TBL_DOCUMENT_TYPE.name}
__table_args: {PersonSchema.NAME}

""")

class DocumentType(BaseModel):
    __tablename__ = PersonSchema.TBL_DOCUMENT_TYPE.name

    __table_args__ = {'schema': PersonSchema.TBL_DOCUMENT_TYPE.schema}

    name = Column(String, nullable=False)

    id_category = Column(Integer, ForeignKey(f'{PersonSchema.TBL_DOCUMENT_CATEGORY.identifier}.id'), nullable=False)
    # 1 document_type -> 1 category
    category = relationship("DocumentCategory", back_populates="list_document_types")

    # 1:N | 1 document_type -> N documents     
    list_documents = relationship("Document", back_populates="document_type")