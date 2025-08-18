from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from app.person.domain.enum.contact_type import EEmailType
from app.person.infrastructure.database.schema import PersonSchema


class Email(BaseModel):
    __tablename__ = PersonSchema.TBL_EMAIL.name
    __table_args__ = {'schema': PersonSchema.TBL_EMAIL.schema}

    id_person = Column(Integer, ForeignKey(f"{PersonSchema.TBL_PERSON.identifier}.id"))
    # 1 email -> 1 person
    person = relationship("Person", back_populates="list_emails")

    type_email = Column(Enum(EEmailType), nullable=False)
    email = Column(String(100), nullable=False)
