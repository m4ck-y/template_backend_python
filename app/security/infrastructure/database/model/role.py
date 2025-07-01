from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from app.security.infrastructure.database.model.permission import permissions_roles
from ..schema import SchemaSecurity

class Role(BaseModel):
    __tablename__ = 'role'

    __table_args__ = {'schema': 'security'}

    key = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True)

    description = Column(Text)
    notes = Column(Text)

    # RELATIONSHIPS

    # N:N | N roles -> N permissions
    list_permissions = relationship(
        "Permission",
        secondary=permissions_roles,
        back_populates="list_roles"
    )