from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaCreateMeasureTypeGroup(ORMModel):
    id_measure_type: int
    id_measure_group: int

class SchemaUpdateMeasureTypeGroup(SchemaCreateMeasureTypeGroup):
    id: int

class SchemaMeasureTypeGroup(SchemaUpdateMeasureTypeGroup):
    pass