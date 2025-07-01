from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum as SqlEnum, Float
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaCompany

class EmployeeMexican(BaseModel):
    __tablename__ = 'employee_mexican'

    __table_args__ = {'schema': 'company'}

    # 1:1 | 1 employee_mexican -> 1 employee
    id_employee = Column(Integer, ForeignKey(f'{SchemaCompany("employee")}.id'), nullable=False, unique=True)
    employee = relationship("Employee", back_populates="employee_mexican")