from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaHealthFacility

class HealthFacility(BaseModel):
    __tablename__ = "health_facility"
    
    # 1:1 | 1 health_facility -> 1 company
    id_company = Column(Integer, ForeignKey("company.id"), nullable=False, unique=True)
    company = relationship("Company")

    key = Column(String(255)) #CLUES
    key_institution = Column(String(255))
    key_establishment_type = Column(String(255))
    key_typology = Column(String(255))
    sanitary_license = Column(String(255))
    patient_nomenclature = Column(String(255))

