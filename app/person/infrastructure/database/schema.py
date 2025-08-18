# Importamos la clase base de SQLAlchemy y la función que detecta si usamos PostgreSQL
from app.config.db import is_db_postgres
from app.utils.infrastructure.database.table_name import TableName

NAME = "person"

class PersonSchema:
    NAME = NAME
    TBL_PERSON = TableName(None, "person") #Schema Publico
    TBL_BIRTH = TableName(NAME, "birth")