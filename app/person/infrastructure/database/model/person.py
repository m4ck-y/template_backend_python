from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from app.config.db import PublicBase
from app.person.domain.enum.gender import EGenderIdentity
from app.utils.enum.verification_status import EVerificationStatus

class Person(PublicBase):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    verification_status = Column(Enum(EVerificationStatus), nullable=False, default=EVerificationStatus.PENDING)
    url_photo = Column(String)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    second_last_name = Column(String)
    type_gender = Column(Enum(EGenderIdentity), nullable=False, default=EGenderIdentity.NO_ESPECIFICADO)