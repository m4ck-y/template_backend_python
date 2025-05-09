# Importamos la clase base de SQLAlchemy y la función que detecta si usamos PostgreSQL
from app.config.db import is_db_postgres

def SchemaHealth(name: str) -> str:
    """
    Devuelve el nombre de la tabla con el prefijo adecuado según el motor de base de datos.
    En PostgreSQL: usa el nombre de la clase en minúsculas con el prefijo 'health.'.
    En SQLite: antepone 'health_' al nombre de la clase.
    """
    if is_db_postgres():
        return f"health.{name.lower()}"  # En PostgreSQL, la tabla está en el esquema 'health'.
    else:
        return f"health_{name.lower()}"  # En SQLite, la tabla tiene el prefijo 'health_'.
