# Importamos la clase base de SQLAlchemy y la función que detecta si usamos PostgreSQL
from config.db import Base, is_db_postgres

# Definimos una clase base abstracta para modelos que pertenecerán al esquema 'person'
class PersonBase(Base):
    __abstract__ = True  # Indica que esta clase no debe ser mapeada como tabla directamente

    @classmethod
    def __tablename__(cls):
        """
        Define dinámicamente el nombre de la tabla en función del tipo de base de datos:
        - En PostgreSQL: simplemente usa el nombre de la clase en minúsculas.
        - En SQLite: antepone 'person_' al nombre para simular un esquema.
        """
        if is_db_postgres():
            return cls.__name__.lower()
        else:
            return f"person_{cls.__name__.lower()}"

    # En PostgreSQL, se especifica que las tablas están en el esquema 'person'.
    # En SQLite, se omite porque no soporta esquemas.
    __table_args__ = {'schema': 'person'} if is_db_postgres() else {}
