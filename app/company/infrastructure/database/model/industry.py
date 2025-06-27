from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaCompany


class Industry(BaseModel):
    """
    Representa una industria o sector económico dentro del dominio empresarial.

    Modela una jerarquía recursiva de industrias. Útil para clasificar empresas
    por sector, ramo o actividad económica con relaciones padre-hijo.

    Atributos:
        name (str): Nombre de la industria. Ej. 'Agroindustria', 'Tecnología'.
        hierarchy (int): ID de la industria padre (nullable).
        description (str): Descripción textual de la industria.
        parent_industry (Industry): Referencia a la industria padre.
        list_subindustries (List[Industry]): Lista de industrias hijas (subsectores).

    Ejemplo de uso:
        >>> tech = Industry(name="Tecnología")
        >>> software = Industry(name="Software", parent_industry=tech)
        >>> tech.list_subindustries  # [Industry(name='Software')]
    """

    __tablename__ = "industry"
    __table_args__ = {'schema': 'company'}
    
    name = Column(String(100), nullable=False)
    hierarchy = Column(Integer, ForeignKey(f'{SchemaCompany("industry")}.id'))
    description = Column(Text)

    parent_industry = relationship("Industry", remote_side="Industry.id", back_populates="list_subindustries")
    list_subindustries = relationship("Industry", back_populates="parent_industry")

    #TODO:  NAICS/INEGI en México.