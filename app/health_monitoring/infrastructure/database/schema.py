# Importamos la clase base de SQLAlchemy y la función que detecta si usamos PostgreSQL
from app.config.db import is_db_postgres
from app.utils.infrastructure.database.table_name import TableName

NAME = "health_monitoring"

class HealthMonitoringSchema:
    NAME = NAME
    TBL_MEASURE_GROUP = TableName(NAME, "measure_group")
    TBL_UNIT = TableName(NAME, "unit")
    TBL_MEASURE_TYPE = TableName(NAME, "measure_type")
    TBL_MEASURE_TYPE_GROUP = TableName(NAME, "measure_type_group")
    TBL_MEASUREMENT = TableName(NAME, "measurement")