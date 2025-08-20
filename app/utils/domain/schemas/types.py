"""
📘 Tipado genérico estándar para entidades del dominio y esquemas Pydantic.

Este módulo define tipos genéricos reutilizables que representan los distintos 
esquemas de una entidad en el backend. Se utilizan tanto para modelos ORM (SQLAlchemy), 
como para validación y transferencia de datos con Pydantic en las capas de infraestructura, 
dominio, aplicación y presentación.

El objetivo es mantener una arquitectura coherente, desacoplada y expresiva 
al trabajar con repositorios, servicios y controladores, siguiendo principios 
de arquitectura limpia, DDD y SOLID.

🧱 Estructura típica:
- TModel: Modelo ORM persistente (SQLAlchemy)
- TSchemaCreateAPI: Esquema de entrada desde la API (POST)
- TSchemaCreateDB: Esquema para crear una entidad en la base de datos
- TSchemaUpdate: Esquema para actualizar una entidad (PUT/PATCH)
- TSchemaItem: Esquema para representar ítems en listados (GET /recurso)
- TSchemaDetail: Esquema para retornar una entidad en detalle (GET /recurso/{id})
"""

from typing import TypeVar
from app.utils.domain.schemas.base_schema import BaseORMModel
from app.utils.infrastructure.database.base_model import BaseModel as TableBaseModel

# ---------------------------------------------------------
# 🧱 Modelo ORM base (SQLAlchemy)
# ---------------------------------------------------------
TModel = TypeVar("TModel", bound=TableBaseModel)
"""
Modelo ORM persistente basado en SQLAlchemy.

Debe heredar de `TableBaseModel`, que extiende `DeclarativeBase`. 
Este tipo se usa para representar entidades del dominio persistidas en la base de datos.

🔧 Ejemplo:
```
    class User(TableBaseModel):
        id: Mapped[int]
        username: Mapped[str]
        email: Mapped[str]
````
"""

# ---------------------------------------------------------
# 📥 Esquema de entrada desde la API (POST)
# ---------------------------------------------------------
TSchemaCreateAPI = TypeVar("TSchemaCreateAPI", bound=BaseORMModel)
"""
Esquema Pydantic recibido desde la API para crear una nueva entidad.

Contiene validaciones de entrada específicas que pueden incluir formatos, reglas de negocio
y estructuras anidadas más amigables para el cliente (frontend o consumidor externo).

🔧 Ejemplo:
```
    class UserCreateAPI(BaseORMModel):
        name: str
        email: str
        address: AddressCreate  # objeto anidado

    class AddressCreate(BaseORMModel):
        zip_code: str
        country_code: str
```
"""

# ---------------------------------------------------------
# 🛠️ Esquema de creación para persistencia en DB (sin anidamiento - plano)
# ---------------------------------------------------------
TSchemaCreateDB = TypeVar("TSchemaCreateDB", bound=BaseORMModel)
"""
Esquema Pydantic para la creación de una entidad en la base de datos.

Este tipo representa los datos ya normalizados, listos para ser persistidos mediante SQLAlchemy.
Se utiliza una estructura plana, alineada con los campos de la tabla correspondiente.

Relaciones a otras entidades se representan como claves foráneas (`*_id`) en lugar de objetos anidados.

🔧 Ejemplo:
````
    class UserCreateDB(BaseORMModel):
        name: str
        email: str
        address_id: int  # relación ya resuelta
```
"""

# ---------------------------------------------------------
# 📋 Esquema de ítem para listados (GET /recurso)
# ---------------------------------------------------------
TSchemaItem = TypeVar("TSchemaItem", bound=BaseORMModel)
"""
Esquema Pydantic para representar un ítem individual dentro de una colección.

Usado en respuestas como `GET /recurso`, proporciona una vista resumida 
de cada entidad. No incluye relaciones ni campos pesados.

🔧 Ejemplo:
```
    class UserItem(BaseORMModel):
        id: int
        username: str
        email: str
```
"""

# ---------------------------------------------------------
# 🔄 Esquema de actualización (entrada - PUT/PATCH)
# ---------------------------------------------------------
TSchemaUpdate = TypeVar("TSchemaUpdate", bound=BaseORMModel)
"""
Esquema Pydantic para actualizar entidades existentes.

Suele incluir el identificador (`id`) y los campos opcionales a modificar. 
Es compatible con operaciones PUT y PATCH.

🔧 Ejemplo:
```
    class UserUpdate(BaseORMModel):
        id: int
        username: Optional[str]
        email: Optional[str]
```
"""

# ---------------------------------------------------------
# 📤 Esquema de retorno en detalle (GET /recurso/{id})
# ---------------------------------------------------------
TSchemaDetail = TypeVar("TSchemaDetail", bound=BaseORMModel)
"""
Esquema Pydantic para retornar una entidad en detalle completo.

Utilizado en endpoints como `GET /recurso/{id}`, este esquema contiene 
campos completos, metadatos, relaciones anidadas, o datos derivados.

```
    class UserDetail(BaseORMModel):
        id: int
        username: str
        email: str
        created_at: datetime
        roles: List[RoleRead]
```
"""