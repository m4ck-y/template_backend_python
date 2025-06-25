from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaHealth

class MeasureTypeGroup(BaseModel):
    __tablename__ = 'measure_type_group'  # Nombre de la tabla

    __table_args__ = {'schema': 'health'}

    id_measure_type = Column(Integer, ForeignKey(f'{SchemaHealth("measure_type")}.id'))
    # 1 measure_type_group -> 1 measure_type
    measure_type = relationship("MeasureType", back_populates="list_measure_type_group")

    id_measure_group = Column(Integer, ForeignKey(f'{SchemaHealth("measure_group")}.id'))
    # 1 measure_type_group -> 1 measure_group
    measure_group = relationship("MeasureGroup", back_populates="list_measure_type_group")