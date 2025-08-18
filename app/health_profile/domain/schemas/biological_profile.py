from app.health_profile.domain.enum.biological_sex import EBiologicalSex
from app.health_profile.domain.enum.blood_type import EBloodType
from app.utils.domain.schemas.basemodel import ORMModel
from pydantic import Field

class SchemaBaseBiologicalProfile(ORMModel):
    id_person: int
    type_biological_sex: EBiologicalSex
    type_blood_type: EBloodType

class SchemaCreateBiologicalProfile(SchemaBaseBiologicalProfile):
    pass

class SchemaUpdateBiologicalProfile(SchemaBaseBiologicalProfile):
    id: int

class SchemaBiologicalProfile(SchemaUpdateBiologicalProfile):
    pass