from app.utils.domain.schemas.basemodel import ORMModel
from app.person.domain.enum.gender import EGenderIdentity
from app.person.domain.schemas.birth import SchemaBirthCreate, SchemaBirth
from app.utils.enum.verification_status import EVerificationStatus
from typing import Union, Optional
from pydantic import Field

class SchemaPersonBase(ORMModel):
    #verification_status: EVerificationStatus
    #url_photo: str = Field(..., examples=["profile.jpg"])#TODO: Service Update Photo
    first_name: str = Field(..., examples=["John"])
    last_name: str = Field(..., examples=["Doe"])
    second_last_name: str = Field(..., examples=["Doe"])
    type_gender: EGenderIdentity

class SchemaPersonCreate(SchemaPersonBase):
    #birth: Optional[SchemaBirthCreate] = None
    pass

class SchemaPersonUpdate(SchemaPersonBase):
    id: int
    verification_status: EVerificationStatus



class SchemaPerson(SchemaPersonUpdate):
    url_photo: Optional[str] = Field(..., examples=["profile.jpg"])
    birth: Union[SchemaBirth, int, None]