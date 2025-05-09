from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaBaseMeasurement(ORMModel):
    id_person: int
    id_measure_type: int
    value: float
    notes: str

class SchemaCreateMeasurement(SchemaBaseMeasurement):
    pass

class SchemaUpdateMeasurement(SchemaBaseMeasurement):
    id: int

class SchemaMeasurement(SchemaBaseMeasurement):
    pass