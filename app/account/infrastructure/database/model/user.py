from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.account.infrastructure.database.schema import AccountSchema
from app.person.infrastructure.database.schema import PersonSchema
from app.utils.infrastructure.database.models.base_model import BaseModel

class User(BaseModel):
    __tablename__ = AccountSchema.TBL_USER.name

    __table_args__ = {"schema": AccountSchema.TBL_USER.schema}

    id_person = Column(Integer, ForeignKey(f"{PersonSchema.TBL_PERSON.identifier}.id"), nullable=False, unique=True)
    # 1:1 | 1 user -> 1 person
    person = relationship("Person", back_populates="user")
    
    username = Column(String(191), nullable=False, unique=True)
    password = Column(String(191), nullable=False)
    
    is_active = Column(Boolean, nullable=False, default=True)

    #TODO: Añadir el resto de campos
    #last_login_at	TIMESTAMP	Último acceso exitoso
    #failed_attempts	INT	Intentos fallidos
    #locked_until	TIMESTAMP	Fecha hasta la cual está bloqueado
