from sqlalchemy import Column, Integer, ForeignKey, Float, Text, DateTime
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModelTimeSeries
from ..schema import SchemaHealth

class Measurement(BaseModelTimeSeries):
    __tablename__ = 'measurement'  # Nombre de la tabla

    __table_args__ = {'schema': 'health'}
    
    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    # 1 Measurement -> 1 Person
    person = relationship("Person", back_populates="list_measurements")

    id_measure_type = Column(Integer, ForeignKey(f'{SchemaHealth("measure_type")}.id'), nullable=False)
    # 1 Measurement -> 1 MeasureType
    measure_type = relationship("MeasureType", back_populates="list_measurements")
    value = Column(Float, nullable=False)
    notes = Column(Text)
