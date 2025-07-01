from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum as SqlEnum, Float
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaCompany

from enum import Enum


class EContractType(int, Enum):
    FULL_TIME = 1    # Tiempo completo
    PART_TIME = 2    # Medio tiempo
    TEMPORARY = 3    # Temporal
    CONTRACTOR = 4   # Freelance/Contratista
    INTERN = 5       # Pasante

class EStatusEmployee(Enum):
    INACTIVE = 0
    "INACTIVO"
    ACTIVE = 1
    "ACTIVO"
    PENDING = 2
    "PENDIENTE"
    SUSPENDED = 4
    "SUSPENDIDO"
    TERMINATED = 5
    "DE BAJA"

class Employee(BaseModel):

    __tablename__ = "employee"

    __table_args__ = {'schema': 'company'}

    id_person = Column(Integer, ForeignKey('person.id'), nullable=False)
    person = relationship("Person", back_populates="list_employments")

    id_company = Column(Integer, ForeignKey('company.id'), nullable=False)
    company = relationship("Company") #TODO: FIX: back_populates="list_employees")

    date_entry = Column(DateTime(timezone=True))
    date_exit = Column(DateTime(timezone=True))

    status = Column(SqlEnum(EStatusEmployee), default=EStatusEmployee.PENDING, nullable=False)
    type_contract = Column(SqlEnum(EContractType), default=EContractType.FULL_TIME, nullable=False)

    score = Column(Float, default=5, nullable=False)


    # RELATIONSHIPS

    # 1:1 | 1 employee -> 1 employee_mexican
    employee_mexican = relationship("EmployeeMexican", back_populates="employee", uselist=False)

