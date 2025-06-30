from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaCompany

class TypeService(BaseModel):
    __tablename__ = "type_service"

    __table_args__ = {'schema': 'company'}

    id_industry = Column(Integer, ForeignKey(f'{SchemaCompany("industry")}.id'), nullable=False)
    industry = relationship("Industry", back_populates="list_type_services")
    name = Column(String(100), nullable=False)