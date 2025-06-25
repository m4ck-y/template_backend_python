from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from app.person.domain.enum.contact_type import EPhoneType
from app.person.infrastructure.database.schema import SchemaPerson

class Phone(BaseModel):
    __tablename__ = "phone"

    __table_args__ = {'schema': 'person'}

    id_person = Column(Integer, ForeignKey('person.id'))
    # 1 phone -> 1 person
    person = relationship("Person", back_populates="list_phones")
    
    type_phone = Column(Enum(EPhoneType), nullable=False)
    code = Column(String(191), nullable=False)#COUNTRY
    number = Column(String(191), nullable=False)