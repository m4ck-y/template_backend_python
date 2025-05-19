# 📦 Repositorio Genérico Base (`BaseRepository`)

**Ubicación:** `app/utils/infrastructure/basecrud.py`

Este módulo contiene una clase genérica reutilizable llamada `BaseRepository`, que proporciona operaciones CRUD comunes para entidades manejadas mediante SQLAlchemy y Pydantic v2. Su objetivo es centralizar lógica compartida y evitar duplicación en los distintos repositorios del proyecto.

---

## 📌 Propósito

Esta clase base permite implementar repositorios rápidamente, asegurando:

- ✅ **Reutilización** de lógica estándar (Create, Read, Update, Delete)
- 🧼 **Limpieza** en los módulos de infraestructura
- 🧪 **Testeo fácil** (una sola clase base testeable)
- ⚙️ **Extensibilidad** para soporte futuro (filtros, paginación, etc.)

---

## 🧠 Diseño y Principios

- Arquitectura orientada a dominio (DDD)
- Principios de Clean Architecture y separación de responsabilidades
- Generics de Python (`TypeVar`) para tipado fuerte y reutilización
- Compatible con SQLAlchemy ORM y Pydantic v2

---

## 🧩 Firma del repositorio

```python
class BaseRepository[
    ModelType,              # Modelo SQLAlchemy (ej. HealthInfo)
    CreateSchemaType,       # Pydantic: Schema de creación
    UpdateSchemaType,       # Pydantic: Schema de actualización
    ReturnSchemaType        # Pydantic: Schema de retorno
]
