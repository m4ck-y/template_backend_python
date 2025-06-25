from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.health.domain.enum.biological_sex import EBiologicalSex
from app.health.domain.enum.blood_type import EBloodType

from ..schema import SchemaHealth

class HealthInfo(BaseModel):
    __tablename__ = 'health_info'

    __table_args__ = {'schema': 'health'}

    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    # 1 person -> 1 health_info
    person = relationship("Person", back_populates="health_info")

    type_biological_sex = Column(Enum(EBiologicalSex), nullable=False)
    type_blood_type = Column(Enum(EBloodType), nullable=False)