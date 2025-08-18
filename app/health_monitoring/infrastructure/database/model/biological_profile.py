from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.health_monitoring.domain.enum.biological_sex import EBiologicalSex
from app.health_monitoring.domain.enum.blood_type import EBloodType


#from app.health_monitoring.infrastructure.database.schema import HealthMonitoringSchema
from app.health_profile.schema import HealthProfileSchema


print(f"""

__tablename: {HealthProfileSchema.TBL_BIOLOGICAL_PROFILE.name}
__table_args: {HealthProfileSchema.NAME}
REFERENCE: {HealthProfileSchema.TBL_BIOLOGICAL_PROFILE.identifier}

""")

class BiologicalProfile(BaseModel):
    __tablename__ = HealthProfileSchema.TBL_BIOLOGICAL_PROFILE.name

    __table_args__ = {'schema': HealthProfileSchema.TBL_BIOLOGICAL_PROFILE.schema}

    id_person = Column(Integer, ForeignKey(F'{HealthProfileSchema.TBL_BIOLOGICAL_PROFILE.identifier}.id'), nullable=False)
    # 1 person -> 1 health_info
    person = relationship("Person", back_populates="biological_profile")

    type_biological_sex = Column(Enum(EBiologicalSex), nullable=False)
    type_blood_type = Column(Enum(EBloodType), nullable=False)