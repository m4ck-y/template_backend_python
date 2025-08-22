from typing import Optional
from pydantic import Field
from app.person.domain.enum.identifier import EIdentifierType
from app.utils.domain.schemas.base_schema import BaseORMModel

class SchemaIdentifierTypeBase(BaseORMModel):
    type_identifier: EIdentifierType = Field(..., examples=[EIdentifierType.NATIONAL])
    name: str = Field(..., examples=["Cédula de Identidad"])
    abbreviation: str = Field(..., examples=["CI"])
    country_code: str = Field(..., examples=["CHL"])

class SchemaCreateAPIIdentifierType(SchemaIdentifierTypeBase):
    pass

class SchemaCreateDBIdentifierType(SchemaIdentifierTypeBase):
    pass

class SchemaItemIdentifierType(SchemaIdentifierTypeBase):
    id: int

class SchemaDetailIdentifierType(SchemaItemIdentifierType):
    pass

class SchemaUpdateIdentifierType(BaseORMModel):
    id: int
    type_identifier: Optional[EIdentifierType] = None
    name: Optional[str] = None
    abbreviation: Optional[str] = None
    country_code: Optional[str] = None
