from app.health.domain.schemas.measure_type_group import SchemaMeasureTypeGroup
from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaBaseMeasureType(ORMModel):
    name : str = Field(..., examples=["Peso", "Altura"])
    id_unit: int

class SchemaCreateMeasureType(SchemaBaseMeasureType):
    pass

class SchemaUpdateMeasureType(SchemaBaseMeasureType):
    id: int


class SchemaMeasureType(SchemaBaseMeasureType):
    list_measure_type_group: list[SchemaUpdateMeasureType]

class SchemaListItemMeasureType(SchemaUpdateMeasureType):
    id: int