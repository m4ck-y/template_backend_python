from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.models.base_model import BaseModel
from app.health_monitoring.infrastructure.database.schema import HealthMonitoringSchema

class MeasureGroup(BaseModel):
    __tablename__ = HealthMonitoringSchema.TBL_MEASURE_GROUP.name

    __table_args__ = {'schema': HealthMonitoringSchema.TBL_MEASURE_GROUP.schema}
    
    name = Column(String(100), unique=True, nullable=False)  # Nombre del grupo

    #RELATIONSHIPS
    # 1:N | measure_group -> measure_type_group
    list_measure_type_group = relationship("MeasureTypeGroup", back_populates="measure_group")