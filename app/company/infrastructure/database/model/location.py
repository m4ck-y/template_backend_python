from sqlalchemy import Column, Float, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from app.utils.infrastructure.database.base_model import BaseModel
from ..schema import SchemaCompany

class Location(BaseModel):
    """
    Modelo para representar la ubicación física de una compañía de forma flexible
    y con posibilidad de internacionalización.

    Este diseño surgió al analizar la necesidad de manejar ubicaciones que contemplen
    diferentes niveles administrativos internacionales, considerando que:

    - Los términos como "estado", "municipio", "asentamiento" varían según el país.
    - No todos los países usan la misma jerarquía ni las mismas divisiones administrativas.
    - Se busca una estructura simple y directa para guardar los datos de localización
      sin crear tablas separadas para cada nivel (país, estado, municipio, etc.).
    - El uso de claves (key_country, key_state, etc.) permite almacenar códigos o abreviaciones
      estandarizadas (por ejemplo, ISO 3166) para facilitar interoperabilidad y validación.
    - Se incluye información adicional como dirección, complemento, código postal y coordenadas GPS.

    La relación con Company es uno a uno, es decir, cada compañía puede tener una sola ubicación
    principal en este esquema. """

    __tablename__ = "location"
    __table_args__ = {"schema": "company"}

    # 1:1 | 1 company -> 1 location
    id_company = Column(Integer, ForeignKey("company.id"), nullable=False, unique=True)
    company = relationship("Company", back_populates="location")

     # Claves o códigos para cada nivel administrativo internacional
    key_country = Column(String(50))        # Código país (ISO 3166-1 alpha-2 recomendado)
    key_state = Column(String(50))          # Código estado/provincia (ISO 3166-2 recomendado)
    key_city = Column(String(50))           # Código de ciudad
    key_municipality = Column(String(50))   # Municipio, alcaldía, delegación o equivalente
    key_neighborhood = Column(String(50))   # Barrio, colonia, localidad o asentamiento

    # Dirección completa y complementos
    address = Column(String(255))            # Dirección principal
    address_complement = Column(String(255))# Complemento de dirección (ej: interior, edificio)

    postal_code = Column(String(20))         # Código postal asociado
    
    # Coordenadas geográficas para ubicación precisa
    latitude = Column(Float)
    longitude = Column(Float)

    #TODO: Para internacionalizar, es muy útil usar códigos estandarizados para países (ISO 3166-1 alpha-2), estados/provincias (ISO 3166-2) y códigos postales cuando existan. Esto facilita validación y compatibilidad.