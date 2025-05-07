from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaUnitBase(ORMModel):
    name: str = Field(..., description="Nombre de la unidad de medida.", examples=["Kilogram", "Meter", "Celsius", "Liter", "Second", "Ampere", "Millimeters of Mercury"])
    symbol: str = Field(..., description="Simbolo de la unidad de medida.", examples=["kg", "m", "°C", "L", "s", "A", "mmHg"])


class SchemaUnitCreate(SchemaUnitBase):
    pass

class SchemaUnitUpdate(SchemaUnitBase):
    id: int

class SchemaUnit(SchemaUnitUpdate):
    pass