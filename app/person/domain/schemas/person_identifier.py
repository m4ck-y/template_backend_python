from typing import Optional
from pydantic import Field
from app.utils.domain.schemas.base_schema import BaseORMModel
from app.person.domain.schemas.identifier_type import SchemaItemIdentifierType

class SchemaPersonIdentifierBase(BaseORMModel):
    identifier_value: str = Field(..., examples=["123456789-0"])

class SchemaCreateAPIPersonIdentifier(SchemaPersonIdentifierBase):
    id_identifier_type: int = Field(..., examples=[1])

class SchemaCreateDBPersonIdentifier(SchemaCreateAPIPersonIdentifier):
    id_person: int

class SchemaItemPersonIdentifier(SchemaPersonIdentifierBase):
    id: int
    id_identifier_type: int

class SchemaDetailPersonIdentifier(SchemaItemPersonIdentifier):
    identifier_type: SchemaItemIdentifierType

class SchemaUpdatePersonIdentifier(BaseORMModel):
    id: int
    identifier_value: Optional[str] = None
    id_identifier_type: Optional[int] = None
