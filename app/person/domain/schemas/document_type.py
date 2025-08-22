from typing import Optional
from pydantic import Field
from app.utils.domain.schemas.base_schema import BaseORMModel
from app.person.domain.schemas.document_category import SchemaItemDocumentCategory

class SchemaDocumentTypeBase(BaseORMModel):
    name: str = Field(..., examples=["Pasaporte"])

class SchemaCreateAPIDocumentType(SchemaDocumentTypeBase):
    id_category: int = Field(..., examples=[1])

class SchemaCreateDBDocumentType(SchemaCreateAPIDocumentType):
    pass

class SchemaItemDocumentType(SchemaDocumentTypeBase):
    id: int
    id_category: int

class SchemaDetailDocumentType(SchemaItemDocumentType):
    category: SchemaItemDocumentCategory

class SchemaUpdateDocumentType(BaseORMModel):
    id: int
    name: Optional[str] = None
    id_category: Optional[int] = None
