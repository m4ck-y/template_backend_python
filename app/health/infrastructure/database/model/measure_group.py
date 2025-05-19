from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaHealth

class MeasureGroup(BaseModel):
    __tablename__ = SchemaHealth('measure_group')  # Nombre de la tabla
    
    name = Column(String(100), unique=True, nullable=False)  # Nombre del grupo

    #RELATIONSHIPS
    # 1:N | measure_group -> measure_type_group
    list_measure_type_group = relationship("MeasureTypeGroup", back_populates="measure_group")