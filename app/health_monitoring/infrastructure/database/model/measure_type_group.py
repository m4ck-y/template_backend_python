from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.health_monitoring.infrastructure.database.schema import HealthMonitoringSchema

class MeasureTypeGroup(BaseModel):
    __tablename__ = HealthMonitoringSchema.TBL_MEASURE_TYPE_GROUP.name

    __table_args__ = {'schema': HealthMonitoringSchema.TBL_MEASURE_TYPE_GROUP.schema}

    id_measure_type = Column(Integer, ForeignKey(f'{HealthMonitoringSchema.TBL_MEASURE_TYPE.identifier}.id'))
    # 1 measure_type_group -> 1 measure_type
    measure_type = relationship("MeasureType", back_populates="list_measure_type_group")

    id_measure_group = Column(Integer, ForeignKey(f'{HealthMonitoringSchema.TBL_MEASURE_GROUP.identifier}.id'))
    # 1 measure_type_group -> 1 measure_group
    measure_group = relationship("MeasureGroup", back_populates="list_measure_type_group")