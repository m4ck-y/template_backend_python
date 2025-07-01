from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaSecurity


permissions_roles = Table(
    'permissions_role',
    BaseModel.metadata,
    Column('id_role', ForeignKey(f'{SchemaSecurity("role")}.id'), nullable=False),
    Column('id_permission', ForeignKey(f'{SchemaSecurity("permission")}.id'), nullable=False),
    schema='security',
)

class Permission(BaseModel):
    __tablename__ = 'permission'
    __table_args__ = {'schema': 'security'}


    id_module = Column(ForeignKey(f'{SchemaSecurity("module")}.id'), nullable=False)
    # 1 permission -> 1 module
    module = relationship("Module", back_populates="list_permissions")
    
    id_action = Column(ForeignKey(f'{SchemaSecurity("action")}.id'), nullable=False)
    # 1 permission -> 1 action
    action = relationship("Action", back_populates="list_permissions")


    #RELATIONSHIPS

    # N:N | N permissions -> N roles
    list_roles = relationship(
        "Role",
        secondary=permissions_roles,
        back_populates="list_permissions"
    )