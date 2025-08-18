from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaBaseMeasureGroup(ORMModel):
    name : str = Field(..., examples=["General", "Circunferencia", "Diametro", "Longitud"])

class SchemaCreateMeasureGroup(SchemaBaseMeasureGroup):
    pass

class SchemaUpdateMeasureGroup(SchemaBaseMeasureGroup):
    id: int

class SchemaMeasureGroup(SchemaUpdateMeasureGroup):
    pass