from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaBirthInfoBase(ORMModel):
    "Without id_person"
    key_birth_country: str = Field(..., description="Clave del país de nacimiento.", examples=["MEX"])
    key_birth_state: str = Field(..., description="Clave del estado de nacimiento.", examples=["01"])
    birth_date: str = Field(..., description="Fecha de nacimiento.", examples=["2001-01-01"])
    birth_date_timezone: str = Field(..., description="Zona horaria de la fecha de nacimiento.", examples=["America/Mexico_City"])

class SchemaBirthInfoCreate(SchemaBirthInfoBase):
    id_person: int

class SchemaBirthInfoUpdate(SchemaBirthInfoBase):
    id: int

class SchemaBirthInfo(SchemaBirthInfoBase):
    id: int
    id_person: int