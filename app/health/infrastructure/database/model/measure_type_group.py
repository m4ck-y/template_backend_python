from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base
from ..base import SchemaHealth

class MeasureTypeGroup(Base):
    __tablename__ = SchemaHealth('measure_type_group')  # Nombre de la tabla

    id_measure_type = Column(Integer, ForeignKey(f'{SchemaHealth("measure_type")}.id'), primary_key=True)
    # 1 measure_type_group -> 1 measure_type
    measure_type = relationship("MeasureType", back_populates="list_measure_type_group")

    id_measure_group = Column(Integer, ForeignKey(f'{SchemaHealth("measure_group")}.id'), primary_key=True)
    # 1 measure_type_group -> 1 measure_group
    measure_group = relationship("MeasureGroup", back_populates="list_measure_type_group")