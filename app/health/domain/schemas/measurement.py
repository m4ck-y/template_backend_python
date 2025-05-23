from typing import Optional
from app.utils.domain.schemas.basemodel import ORMTimeSeries
from pydantic import Field

class SchemaBaseMeasurement(ORMTimeSeries):
    id_person: int
    id_measure_type: int
    value: float
    notes: Optional[str] = None

class SchemaCreateMeasurement(SchemaBaseMeasurement):
    pass

class SchemaUpdateMeasurement(SchemaBaseMeasurement):
    id: int

class SchemaMeasurement(SchemaUpdateMeasurement):
    pass