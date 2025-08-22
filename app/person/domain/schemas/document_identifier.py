from typing import Optional
from pydantic import Field
from app.utils.domain.schemas.base_schema import BaseORMModel
from app.person.domain.schemas.person_identifier import SchemaItemPersonIdentifier
from app.person.domain.schemas.document import SchemaItemDocument

class SchemaDocumentIdentifierBase(BaseORMModel):
    pass

class SchemaCreateAPIDocumentIdentifier(SchemaDocumentIdentifierBase):
    id_person_identifier: int = Field(..., examples=[1])
    id_document: int = Field(..., examples=[1])

class SchemaCreateDBDocumentIdentifier(SchemaCreateAPIDocumentIdentifier):
    pass

class SchemaItemDocumentIdentifier(SchemaCreateAPIDocumentIdentifier):
    id: int

class SchemaDetailDocumentIdentifier(SchemaItemDocumentIdentifier):
    person_identifier: SchemaItemPersonIdentifier
    document: SchemaItemDocument

class SchemaUpdateDocumentIdentifier(BaseORMModel):
    id: int
    id_person_identifier: Optional[int] = None
    id_document: Optional[int] = None
