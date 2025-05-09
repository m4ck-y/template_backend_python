from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.config.db import BaseModel
from app.person.domain.enum.contact_type import EEmailType
from app.person.infrastructure.database.schema import SchemaPerson


class Email(BaseModel):
    __tablename__ = SchemaPerson("email")
    id = Column(Integer, primary_key=True)

    id_person = Column(Integer, ForeignKey("person.id"))
    # 1 email -> 1 person
    person = relationship("Person", back_populates="list_emails")

    type_email = Column(Enum(EEmailType), nullable=False)
    email = Column(String(100), nullable=False)
