from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaSecurity

class Module(BaseModel):
    __tablename__ = 'module'

    __table_args__ = {'schema': 'security'}

    key = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True)

    list_permissions = relationship("Permission", back_populates="module")