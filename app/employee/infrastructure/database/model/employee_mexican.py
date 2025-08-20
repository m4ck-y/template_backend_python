from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum as SqlEnum, Float
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.models.base_model import BaseModel
from ..schema import SchemaEmployee


from enum import Enum

class YesNoStatus(Enum):
    NO = 0
    YES = 1

class EmployeeMexican(BaseModel):
    __tablename__ = 'employee_mexican'

    __table_args__ = {'schema': 'employee'}

    programaSMyMG = Column(SqlEnum(YesNoStatus), default=YesNoStatus.NO, nullable=False)
    """programaSMyMG

    Si para el valor registrado en la variable “clues”, en la columna de institucion es igual a “SSA” o “IMB” de acuerdo al catálogo de ESTABLECIMIENTO DE SALUD SIS, se debe registrar una de las siguientes opciones: 
    - 0 – NO
    - 1 – SI
    """

    # 1:1 | 1 employee_mexican -> 1 employee
    id_employee = Column(Integer, ForeignKey("employee.id"), nullable=False, unique=True)
    employee = relationship("Employee", back_populates="employee_mexican")