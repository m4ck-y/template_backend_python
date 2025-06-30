from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from app.person.domain.enum.gender import EGenderIdentity
from app.utils.enum.verification_status import EVerificationStatus
from ..schema import SchemaAccount

class User(BaseModel):
    __tablename__ = "user"

    __table_args__ = {"schema": "account"}

    id_person = Column(Integer, ForeignKey("person.id"), nullable=False, unique=True)
    person = relationship("Person", back_populates="user")
    
    username = Column(String(191), nullable=False, unique=True)
    password = Column(String(191), nullable=False)
    
    is_active = Column(Boolean, nullable=False, default=True)

    #TODO: Añadir el resto de campos
    #last_login_at	TIMESTAMP	Último acceso exitoso
    #failed_attempts	INT	Intentos fallidos
    #locked_until	TIMESTAMP	Fecha hasta la cual está bloqueado
