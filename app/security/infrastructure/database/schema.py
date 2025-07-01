from app.config.db import is_db_postgres

def SchemaSecurity(name: str) -> str:
    """
    Devuelve el nombre de la tabla con el prefijo adecuado según el motor de base de datos.
    En PostgreSQL: usa el nombre de la clase en minúsculas con el prefijo 'health.'.
    En SQLite: antepone 'health_' al nombre de la clase.
    """
    if is_db_postgres():
        return f"security.{name.lower()}"
    else:
        return ""
