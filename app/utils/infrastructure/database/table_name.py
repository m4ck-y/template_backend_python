from app.config.db import is_db_postgres

class TableName:
    """
    Representa una tabla dentro de un esquema, adaptándose al motor de base de datos actual.

    ✅ PostgreSQL → usa nombres normales con esquema real.

    ✅ SQLite → simula esquema usando prefijos (ej: `person_table_name`).
    """

    def __init__(self, schema: str | None, raw: str):
        """
        Inicializa una nueva instancia de TableName.

        Args:
            schema (str | None): Nombre del esquema lógico al que pertenece la tabla.
                                 Si es None, se asume sin esquema (cadena vacía).
            raw (str): Nombre crudo de la tabla (sin prefijo ni esquema).
        """
        self._schema = schema if schema is not None else ""
        self._raw = raw.lower()

    @property
    def name(self) -> str:
        """
        Nombre de la tabla para usar en `__tablename__`.

        Returns:
            str:
                - PostgreSQL → "document"
                - SQLite → "person_document"
        """
        if is_db_postgres():
            return self._raw
        elif not self._schema:
            return self._raw  # no tiene prefijo en SQLite
        else:
            return f"{self._schema}_{self._raw}"

    @property
    def schema(self) -> str | None:
        """
        Nombre del esquema, para usar en `__table_args__`.

        Returns:
            str | None:
                - PostgreSQL → "person"
                - SQLite → None
        """
        if is_db_postgres():
            return None if not self._schema else self._schema
        else:
            return None

    @property
    def dotted(self) -> str:
        """
        Representación con punto: schema.tabla

        Returns:
            str: Ejemplo → "health.measure_type"
        """
        if self._schema:
            return f"{self._schema}.{self._raw}"
        else:
            return self._raw

    @property
    def prefixed(self) -> str:
        """
        Representación con guion bajo: schema_tabla

        Returns:
            str: Ejemplo → "health_measure_type"
        """
        if self._schema:
            return f"{self._schema}_{self._raw}"
        else:
            return self._raw

    @property
    def identifier(self) -> str:
        """
        Nombre completo de la tabla para usar en ForeignKey, expresiones SQL, etc.

        Returns:
            str:
                - PostgreSQL:
                    - Si esquema vacío → "document"
                    - Si otro esquema → "person.document"
                - SQLite:
                    - Si esquema vacío → "document"
                    - Si otro esquema → "person_document"
        """
        if is_db_postgres():
            return self._raw if not self._schema else f"{self._schema}.{self._raw}"
        else:
            return self._raw if not self._schema else f"{self._schema}_{self._raw}"

    def __str__(self) -> str:
        """
        Permite usar la instancia directamente como `str`.

        Returns:
            str: Igual que `.name`
        """
        return self.name

