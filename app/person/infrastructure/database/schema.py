# Importamos la clase base de SQLAlchemy y la función que detecta si usamos PostgreSQL
from app.config.db import is_db_postgres
from app.utils.infrastructure.database.table_name import TableName

def SchemaPerson(name: str) -> str:
    """
    Devuelve el nombre de la tabla con el prefijo adecuado según el motor de base de datos.
    - En PostgreSQL: usa el esquema 'person' (ej: 'person.table_name').
    - En otros motores (como SQLite): devuelve solo el nombre de la tabla.
    """
    if is_db_postgres():
        return f"person.{name.lower()}"  # En PostgreSQL, la tabla está en el esquema 'person'.
    else:
        #return f"person_{name.lower()}"  # En SQLite, la tabla tiene el prefijo 'person_'.
        return ""

class PersonSchema:
    NAME = "person"
    TBL_PERSON = TableName(None, "person") #Schema Publico
    TBL_BIRTH_INFO = TableName(NAME, "birth_info")