from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.config.db import Base
from app.person.domain.enum.contact_type import EAddressType
from app.person.infrastructure.database.model.base import SchemaPerson

class Address(Base):
    __tablename__ = SchemaPerson('address')
    id = Column(Integer, primary_key=True, autoincrement=True)

    id_person = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="list_addresses")

    type_address = Column(Enum(EAddressType), nullable=False)

    key_country = Column(String(20))
    key_state = Column(String(20)) #Estado, provincia o región.
    key_municipality = Column(String(20))
    key_locality = Column(String(20))
    address = Column(String(191))#address_line1: Primera línea de la dirección (calle y número).
    complement = Column(String(191))#address_line2: Segunda línea de la dirección (opcional, para información adicional).
    postal_code = Column(String(191))
    latitud = Column(Float)
    longitud = Column(Float)
