📘 README – Clase TableName: Gestión Escalable y Portátil de Esquemas y Tablas en SQLAlchemy
🎯 Objetivo

La clase TableName fue diseñada para resolver un problema común en entornos donde se necesita soportar múltiples motores de base de datos (como PostgreSQL y SQLite), manteniendo una arquitectura limpia, modular y escalable basada en schemas lógicos.

🤔 ¿Por qué TableName?

En motores como PostgreSQL, puedes organizar tablas dentro de schemas, lo cual permite separar dominios como person, health, admin, etc.

En SQLite, no existen schemas, por lo que todas las tablas comparten el mismo espacio de nombres. Esto genera conflictos si intentamos tener dos tablas con el mismo nombre en distintos schemas.

La clase TableName actúa como un adaptador de nombres de tabla según el motor actual, y se utiliza para:

Asignar correctamente __tablename__

Establecer __table_args__['schema'] solo cuando es necesario

Construir claves foráneas (ForeignKey) de forma segura

Mantener la portabilidad y evitar errores de colisión de nombres

🛠 Métodos de TableName
Método	Descripción breve
.name	Nombre de la tabla a usar en __tablename__
.schema	Nombre del esquema a usar en __table_args__['schema']
.identifier	Nombre completo a usar en claves foráneas (schema.tabla o schema_tabla)
.dotted	Representación en formato schema.table
.prefixed	Representación en formato schema_table
__str__()	Devuelve automáticamente .name cuando se usa como string
📦 ¿Dónde y cómo se usa?
1. __tablename__

Se utiliza para asignar el nombre real de la tabla en SQLAlchemy.
La lógica interna del método .name permite que se use el nombre apropiado según el motor actual.

2. __table_args__['schema']

Se aplica solo si el motor lo requiere (ej. PostgreSQL).
SQLite ignora esta opción, y la clase TableName se asegura de devolver None si no aplica.

3. ForeignKey (.identifier)

Es crucial para construir claves foráneas sin errores.
TableName.identifier asegura que el nombre sea correcto y compatible según el motor.

📌 Ejemplo de uso aplicado (sin código)
Modelo BirthInfo

Este modelo representa información de nacimiento de una persona.

Usa __tablename__ = TableName.name para nombrar la tabla correctamente según el motor.

Usa __table_args__ = {'schema': TableName.schema} para declarar el esquema solo si es necesario.

Declara una clave foránea hacia la tabla Person utilizando TableName.identifier para asegurar portabilidad.

Establece una relación uno a uno con el modelo Person.

Representación lógica:
class BirthInfo(BaseModel):
    __tablename__ = [TableName.name de person_birth_info]
    __table_args__ = {"schema": [TableName.schema de person_birth_info]}

    id_person = Column(Integer, ForeignKey([TableName.identifier de person], nullable=False, unique=True))

    # 1:1 | 1 birth_info → 1 person
    person = relationship("Person", back_populates="birth_info")

💡 Beneficios del enfoque
Beneficio	Explicación
✅ Portabilidad	Sin cambios de código entre PostgreSQL y SQLite
✅ Escalabilidad	Puedes agregar más schemas/tablas sin conflictos
✅ DRY	Evitas repetir strings y nombres manualmente
✅ Legibilidad	El código expresa claramente la intención de diseño modular
✅ Seguridad	Las claves foráneas se construyen correctamente en cualquier motor
🧼 Recomendaciones de uso

Usa .name para __tablename__.

Usa .schema únicamente en __table_args__.

Usa .identifier para ForeignKey(...) y expresiones SQL.

Nunca escribas manualmente strings como "person.document" o "person_document". Centraliza todo con TableName.

✅ Conclusión

La existencia y desarrollo de la clase TableName permite:

Evitar errores típicos al cambiar entre motores de base de datos.

Mantener una arquitectura modular basada en schemas.

Desarrollar de forma limpia y escalable en proyectos complejos.

Abstraer las diferencias del motor y centrarte en el modelo de datos, no en las limitaciones técnicas del motor.

🧠 Piensa en esquemas como namespaces, y en TableName como el traductor entre tu diseño lógico y la implementación física en SQL.