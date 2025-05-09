from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.config.db import BaseModel
from ..schema import SchemaHealth

class MeasureGroup(BaseModel):
    __tablename__ = SchemaHealth('measure_group')  # Nombre de la tabla

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)  # Nombre del grupo

    #RELATIONSHIPS
    # 1:N | measure_group -> measure_type_group
    list_measure_type_group = relationship("MeasureTypeGroup", back_populates="measure_group")