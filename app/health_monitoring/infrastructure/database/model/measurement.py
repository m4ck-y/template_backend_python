from sqlalchemy import Column, Integer, ForeignKey, Float, Text, DateTime
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModelTimeSeries
from app.health_monitoring.infrastructure.database.schema import HealthMonitoringSchema
from app.person.infrastructure.database.schema import PersonSchema

class Measurement(BaseModelTimeSeries):
    __tablename__ = HealthMonitoringSchema.TBL_MEASUREMENT.name

    __table_args__ = {'schema': HealthMonitoringSchema.TBL_MEASUREMENT.schema}

    id_person = Column(Integer, ForeignKey(f'{PersonSchema.TBL_PERSON.identifier}.id'), nullable=False)
    # 1 Measurement -> 1 Person
    person = relationship("Person", back_populates="list_measurements")

    id_measure_type = Column(Integer, ForeignKey(f'{HealthMonitoringSchema.TBL_MEASURE_TYPE.identifier}.id'), nullable=False)
    # 1 Measurement -> 1 MeasureType
    measure_type = relationship("MeasureType", back_populates="list_measurements")
    value = Column(Float, nullable=False)
    notes = Column(Text)
