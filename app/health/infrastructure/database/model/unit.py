from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaHealth

class Unit(BaseModel):
    __tablename__ = 'unit' # Nombre de la tabla

    __table_args__ = {'schema': 'health'}

    name = Column(String(50), unique=True, nullable=False)  # Nombre de la unidad (ej. kg, m, °C)
    symbol = Column(String(10))  # Símbolo de la unidad

    #RELATIONSHIPS
    # 1:N | 1 unit -> N measure_type
    list_measure_types = relationship("MeasureType", back_populates="unit")