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


    #RELATIONSHIPS
    # 1:1 | 1 person -> 1 birth_info
    birth_info = relationship("BirthInfo", back_populates="person", uselist=False)
    # 1:1 | 1 person -> 1 sociocultural_identity
    sociocultural_identity = relationship("SocioculturalIdentity", back_populates="person", uselist=False)
    # 1:1 | 1 person -> 1 legal_info
    legal_info = relationship("LegalInfo", back_populates="person", uselist=False)

    # 1:N | 1 person -> N person_identifier
    list_person_identifiers = relationship("PersonIdentifier", back_populates="person")
    # 1:N | 1 person -> N document
    list_documents = relationship("Document", back_populates="person")




    #user = relationship("User", back_populates="person", uselist=False)
    #profile = relationship("Profile", back_populates="person", uselist=False)
    #person_metrics = relationship("PersonMetrics", back_populates="person")