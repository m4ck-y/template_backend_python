from typing import Optional
from pydantic import Field
from app.person.domain.enum.contact_type import EPhoneType
from app.utils.domain.schemas.base_schema import BaseORMModel

class SchemaPhoneBase(BaseORMModel):
    type_phone: EPhoneType = Field(..., examples=[EPhoneType.CELULAR])
    code: str = Field(..., examples=["+52"])
    number: str = Field(..., examples=["5512345678"])

class SchemaCreateAPIPhone(SchemaPhoneBase):
    pass

class SchemaCreateDBPhone(SchemaPhoneBase):
    id_person: int

class SchemaItemPhone(SchemaPhoneBase):
    id: int

class SchemaDetailPhone(SchemaItemPhone):
    pass

class SchemaUpdatePhone(BaseORMModel):
    id: int
    type_phone: Optional[EPhoneType] = None
    code: Optional[str] = None
    number: Optional[str] = None
