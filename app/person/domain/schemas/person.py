from app.person.domain.enum.gender import EGenderIdentity
from app.person.domain.schemas.birth import SchemaBirth
from app.utils.enum.verification_status import EVerificationStatus
from app.utils.domain.schemas.base_schema import BaseORMModel
from typing import Union, Optional
from pydantic import Field

class SchemaPersonBase(BaseORMModel):
    first_name: str = Field(..., examples=["John"])
    last_name: str = Field(..., examples=["Doe"])
    second_last_name: str = Field(..., examples=["Doe"])
    type_gender: EGenderIdentity

class SchemaCreateAPIPerson(SchemaPersonBase):
    #birth: Optional[SchemaBirthCreate] = None
    pass

class SchemaCreateDBPerson(SchemaPersonBase):
    pass

class SchemaItemPerson(SchemaPersonBase):
    verification_status: EVerificationStatus
    url_photo: Optional[str] = Field(..., examples=["profile.jpg"])#TODO: Service Update Photo
    id: int


class SchemaDetailPerson(SchemaItemPerson):
    birth: Union[SchemaBirth, int, None]

class SchemaPersonUpdate(SchemaPersonBase):
    id: int
    verification_status: EVerificationStatus