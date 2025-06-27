# Importamos la clase base de SQLAlchemy y la función que detecta si usamos PostgreSQL
from app.config.db import is_db_postgres

def SchemaCompany(name: str) -> str:
    if is_db_postgres():
        return f"company.{name.lower()}"  # En PostgreSQL, la tabla está en el esquema 'person'.
    else:
        #return f"person_{name.lower()}"  # En SQLite, la tabla tiene el prefijo 'person_'.
        return ""