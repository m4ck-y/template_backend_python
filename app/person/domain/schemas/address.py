from typing import Optional
from pydantic import Field
from app.person.domain.enum.contact_type import EAddressType
from app.utils.domain.schemas.base_schema import BaseORMModel

class SchemaAddressBase(BaseORMModel):
    type_address: EAddressType = Field(..., examples=[EAddressType.DOMICILIO])
    key_country: Optional[str] = Field(None, examples=["MEX"])
    key_state: Optional[str] = Field(None, examples=["MEX-CMX"])
    key_municipality: Optional[str] = Field(None, examples=["010"])
    key_locality: Optional[str] = Field(None, examples=["0001"])
    address: Optional[str] = Field(None, examples=["Av. Insurgentes Sur 123"])
    complement: Optional[str] = Field(None, examples=["Piso 4, Depto 402"])
    postal_code: Optional[str] = Field(None, examples=["06600"])
    latitud: Optional[float] = Field(None, examples=[19.4326])
    longitud: Optional[float] = Field(None, examples=[-99.1332])

class SchemaCreateAPIAddress(SchemaAddressBase):
    pass

class SchemaCreateDBAddress(SchemaAddressBase):
    id_person: int

class SchemaItemAddress(SchemaAddressBase):
    id: int

class SchemaDetailAddress(SchemaItemAddress):
    pass

class SchemaUpdateAddress(BaseORMModel):
    id: int
    type_address: Optional[EAddressType] = None
    key_country: Optional[str] = None
    key_state: Optional[str] = None
    key_municipality: Optional[str] = None
    key_locality: Optional[str] = None
    address: Optional[str] = None
    complement: Optional[str] = None
    postal_code: Optional[str] = None
    latitud: Optional[float] = None
    longitud: Optional[float] = None
