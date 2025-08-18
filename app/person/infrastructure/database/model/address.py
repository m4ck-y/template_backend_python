from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.utils.infrastructure.database.base_model import BaseModel
from app.person.domain.enum.contact_type import EAddressType
from app.person.infrastructure.database.schema import PersonSchema

class Address(BaseModel): #TODO: checar con otro repositorio server_data, columnas
    __tablename__ = PersonSchema.TBL_ADDRESS.name

    __table_args__ = {'schema': PersonSchema.TBL_ADDRESS.schema}

    id_person = Column(Integer, ForeignKey(f"{PersonSchema.TBL_PERSON.identifier}.id"))
    # 1 address -> 1 person
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
