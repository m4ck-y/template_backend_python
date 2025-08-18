# �E️ TableName - Adaptador Multi-Motor para SQLAlchemy

## 🎯 Propósito

Clase utilitaria que abstrae las diferencias entre motores de base de datos para el manejo de esquemas y nombres de tabla, garantizando portabilidad entre PostgreSQL y SQLite.

## 🔧 Problema que Resuelve

- **PostgreSQL:** Soporta esquemas reales (`person.birth`)
- **SQLite:** No tiene esquemas, requiere prefijos (`person_birth`)

TableName unifica ambos enfoques automáticamente según el motor detectado.

## 📋 Propiedades Principales

| Propiedad | PostgreSQL | SQLite | Uso |
|-----------|------------|--------|-----|
| `.name` | `birth` | `person_birth` | `__tablename__` |
| `.schema` | `person` | `None` | `__table_args__['schema']` |
| `.identifier` | `person.birth` | `person_birth` | `ForeignKey()` |

## 💻 Ejemplo de Uso

```python
# Definición del esquema
class PersonSchema:
    NAME = "person"
    TBL_PERSON = TableName(None, "person")    # Esquema público
    TBL_BIRTH = TableName(NAME, "birth")      # Esquema person

# Modelo SQLAlchemy
class Birth(BaseModel):
    __tablename__ = PersonSchema.TBL_BIRTH.name
    __table_args__ = {'schema': PersonSchema.TBL_BIRTH.schema}
    
    # Clave foránea portable
    id_person = Column(Integer, 
                      ForeignKey(f"{PersonSchema.TBL_PERSON.identifier}.id"),
                      nullable=False, unique=True)
```

## ✅ Beneficios

- **Portabilidad:** Código idéntico funciona en PostgreSQL y SQLite
- **DRY:** Centraliza la lógica de nombres de tabla
- **Seguridad:** Previene errores de referencia entre tablas
- **Escalabilidad:** Facilita agregar nuevos esquemas y tablas

## 🎯 Reglas de Uso

1. **Siempre** usar `.name` para `__tablename__`
2. **Siempre** usar `.schema` para `__table_args__['schema']`
3. **Siempre** usar `.identifier` para `ForeignKey()`
4. **Nunca** hardcodear nombres como `"person.document"`