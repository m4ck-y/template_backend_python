from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.config.db import Base
from app.person.domain.enum.contact_type import EPhoneType
from app.person.infrastructure.database.model.base import SchemaPerson

class Phone(Base):
    __tablename__ = SchemaPerson("phone")
    id = Column(Integer, primary_key=True, autoincrement=True)

    id_user = Column(Integer, ForeignKey('person.id'))
    user = relationship("Person", back_populates="list_phones")
    
    type_phone = Column(Enum(EPhoneType), nullable=False)
    code = Column(String(191), nullable=False)#COUNTRY
    number = Column(String(191), nullable=False)