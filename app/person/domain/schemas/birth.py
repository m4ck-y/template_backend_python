from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaBirthBase(ORMModel):
    """Base schema for birth information without id_person."""
    key_birth_country: str = Field(..., description="Clave del país de nacimiento.", examples=["MEX"])
    key_birth_state: str = Field(..., description="Clave del estado de nacimiento.", examples=["01"])
    birth_date: str = Field(..., description="Fecha de nacimiento.", examples=["2001-01-01"])
    birth_date_timezone: str = Field(..., description="Zona horaria de la fecha de nacimiento.", examples=["America/Mexico_City"])

class SchemaBirthCreate(SchemaBirthBase):
    """Schema for creating birth information."""
    id_person: int

class SchemaBirthUpdate(SchemaBirthBase):
    """Schema for updating birth information."""
    id: int

class SchemaBirth(SchemaBirthBase):
    """Complete birth information schema."""
    id: int
    id_person: int