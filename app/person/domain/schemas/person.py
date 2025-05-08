from app.utils.domain.schemas.basemodel import ORMModel
from app.person.domain.enum.gender import EGenderIdentity
from app.person.domain.schemas.birth_info import SchemaBirthInfoCreate, SchemaBirthInfo
from app.utils.enum.verification_status import EVerificationStatus
from typing import Union, Optional
from pydantic import Field

class SchemaPersonBase(ORMModel):
    #verification_status: EVerificationStatus
    url_photo: str = Field(..., examples=["profile.jpg"])
    first_name: str = Field(..., examples=["John"])
    last_name: str = Field(..., examples=["Doe"])
    second_last_name: str = Field(..., examples=["Doe"])
    type_gender: EGenderIdentity

class SchemaPersonCreate(SchemaPersonBase):
    #birth_info: Optional[SchemaBirthInfoCreate] = None
    pass

class SchemaPersonUpdate(SchemaPersonBase):
    id: int
    verification_status: EVerificationStatus



class SchemaPerson(SchemaPersonBase):
    birth_info: Union[SchemaBirthInfo, int, None]