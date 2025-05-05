from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.config.db import Base
from ..base import SchemaHealth

class Unit(Base):
    __tablename__ = SchemaHealth('unit') # Nombre de la tabla

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)  # Nombre de la unidad (ej. kg, m, °C)
    symbol = Column(String(10))  # Símbolo de la unidad

    #RELATIONSHIPS
    # 1:N | 1 unit -> N measure_type
    list_measure_types = relationship("MeasureType", back_populates="unit")