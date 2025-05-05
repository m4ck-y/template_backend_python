from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base
from app.health.domain.enum.biological_sex import EBiologicalSex
from app.health.domain.enum.blood_type import EBloodType

from ..base import SchemaHealth

class HealthInfo(Base):
    __tablename__ = SchemaHealth('health_info')

    id = Column(Integer, primary_key=True)

    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    # 1 person -> 1 health_info
    person = relationship("Person", back_populates="health_info")

    type_biological_sex = Column(Enum(EBiologicalSex), nullable=False)
    type_blood_type = Column(Enum(EBloodType), nullable=False)