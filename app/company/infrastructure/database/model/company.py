from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from app.company.domain.enum.organization_size import EOrganizationSize
from app.company.domain.enum.type_organization import EOrganizationType
from app.utils.infrastructure.database.models.base_model import BaseModel
from ..schema import SchemaCompany


class Company(BaseModel):
    __tablename__ = "company"

    name = Column(String(100), nullable=False) # NAME LARGE, INSTITUTO MEXICANO DEL SEGURO SOCIAL
    legal_name = Column(String(255))# RAZON SOCIAL: SA DE CV
    commercial_name = Column(String(255)) # NAME SHORT: IMSS
    fiscal_id = Column(String(255))# RFC
 
    url_website = Column(String(255))
    url_logo = Column(String(255))
    tagline = Column(String(255))

    id_industry = Column(Integer, ForeignKey(f'{SchemaCompany("industry")}.id'), nullable=False) # id_industry = Column(Integer, ForeignKey('industry.id'))
    industry = relationship("Industry", back_populates="list_companies")

    organization_size = Column(Enum(EOrganizationSize))
    type_organization = Column(Enum(EOrganizationType))

    
    # CIRCULAR REFERENCE
    # parent
    id_parent_company = Column(Integer, ForeignKey('company.id'))
    parent_company = relationship("Company", remote_side="Company.id", back_populates="list_subcompanies")
    # children
    list_subcompanies = relationship("Company",  back_populates="parent_company")

    # RELATIONSHIP
    # 1:1 | 1 company -> 1 location
    location = relationship("Location", uselist=False, back_populates="company")

    # 1:N | 1 company -> N employees
    list_employees = relationship("Employee", back_populates="company")