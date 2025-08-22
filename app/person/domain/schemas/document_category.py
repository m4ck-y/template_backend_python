from typing import Optional
from pydantic import Field
from app.utils.domain.schemas.base_schema import BaseORMModel

class SchemaDocumentCategoryBase(BaseORMModel):
    name: str = Field(..., examples=["Identificación Oficial"])

class SchemaCreateAPIDocumentCategory(SchemaDocumentCategoryBase):
    pass

class SchemaCreateDBDocumentCategory(SchemaDocumentCategoryBase):
    pass

class SchemaItemDocumentCategory(SchemaDocumentCategoryBase):
    id: int

class SchemaDetailDocumentCategory(SchemaItemDocumentCategory):
    pass

class SchemaUpdateDocumentCategory(BaseORMModel):
    id: int
    name: Optional[str] = None
