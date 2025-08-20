from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.models.base_model import BaseModel
from app.health_monitoring.infrastructure.database.schema import HealthMonitoringSchema

class MeasureType(BaseModel):
    __tablename__ = HealthMonitoringSchema.TBL_MEASURE_TYPE.name

    __table_args__ = {'schema': HealthMonitoringSchema.TBL_MEASURE_TYPE.schema}

    name = Column(String(100), nullable=False)  # Nombre del tipo de medición

    id_unit = Column(Integer, ForeignKey(f'{HealthMonitoringSchema.TBL_UNIT.identifier}.id'), nullable=False)  # Relación con la unidad
    # 1:1 | 1 measure_type -> 1 unit
    unit = relationship('Unit', back_populates='list_measure_types')

    #RELATIONSHIPS
    # 1:N | 1 measure_type -> N measure_type_group
    list_measure_type_group = relationship("MeasureTypeGroup", back_populates="measure_type")

    # 1:N | 1 measure_type -> N measurement
    list_measurements = relationship("Measurement", back_populates="measure_type")
