from sqlalchemy import Column, Integer, String, Enum
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

    birth_info = relationship("BirthInfo", back_populates="person", uselist=False)
    sociocultural_identity = relationship("SocioculturalIdentity", back_populates="person", uselist=False)
    legal_info = relationship("LegalInfo", back_populates="person", uselist=False)
    user = relationship("User", back_populates="person", uselist=False)
    profile = relationship("Profile", back_populates="person", uselist=False)
    person_metrics = relationship("PersonMetrics", back_populates="person")