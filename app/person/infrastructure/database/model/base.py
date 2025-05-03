# Importamos la clase base de SQLAlchemy y la función que detecta si usamos PostgreSQL
from app.config.db import is_db_postgres

def SchemaPerson(name: str) -> str:
    """
    Devuelve el nombre de la tabla con el prefijo adecuado según el motor de base de datos.
    En PostgreSQL: usa el nombre de la clase en minúsculas con el prefijo 'person.'.
    En SQLite: antepone 'person_' al nombre de la clase.
    """
    if is_db_postgres():
        return f"person.{name.lower()}"  # En PostgreSQL, la tabla está en el esquema 'person'.
    else:
        return f"person_{name.lower()}"  # En SQLite, la tabla tiene el prefijo 'person_'.