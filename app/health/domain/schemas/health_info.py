from app.health.domain.enum.biological_sex import EBiologicalSex
from app.health.domain.enum.blood_type import EBloodType
from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaBaseHealthInfo(ORMModel):
    id_person: int
    type_biological_sex: EBiologicalSex
    type_blood_type: EBloodType

class SchemaCreateHealthInfo(SchemaBaseHealthInfo):
    pass

class SchemaUpdateHealthInfo(SchemaBaseHealthInfo):
    id: int

class SchemaHealthInfo(SchemaUpdateHealthInfo):
    pass