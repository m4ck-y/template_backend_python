from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.health.infrastructure.database.base import SchemaHealth
from app.config.db import Base

class MeasureType(Base):
    __tablename__ = SchemaHealth('measure_type')

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)  # Nombre del tipo de medición

    id_unit = Column(Integer, ForeignKey(f'{SchemaHealth("unit")}.id'), nullable=False)  # Relación con la unidad
    # 1 measure_type -> 1 unit
    unit = relationship('Unit', back_populates='list_measure_types')

    #RELATIONSHIPS
    # 1:N | 1 measure_type -> N measure_type_group
    list_measure_type_group = relationship("MeasureTypeGroup", back_populates="measure_type")

    # 1:N | 1 measure_type -> N measurement
    list_measurements = relationship("Measurement", back_populates="measure_type")
