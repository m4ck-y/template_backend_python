# Importamos la clase base de SQLAlchemy y la función que detecta si usamos PostgreSQL
from app.config.db import is_db_postgres

def SchemaHealthFacility(name: str) -> str:
    if is_db_postgres():
        return f"health_facility.{name.lower()}"
    else:
        return ""