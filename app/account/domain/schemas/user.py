#from typing import Optional
from pydantic import Field
from app.utils.domain.schemas.base_schema import BaseORMModel
from app.person.domain.schemas.person import SchemaDetailPerson

class SchemaUserBase(BaseORMModel):
    """
    Esquema base para un usuario del sistema.
    """
    username: str = Field(..., examples=["john.doe"], description="Nombre de usuario único en el sistema.")
    is_active: bool = Field(True, description="Indica si el usuario está activo.")

class SchemaCreateAPIUser(SchemaUserBase):
    """
    Esquema para crear un usuario desde la API.
    """
    id_person: int = Field(..., description="ID de la persona asociada a este usuario.")
    password: str = Field(..., description="Contraseña en texto plano.")

class SchemaCreateDBUser(SchemaUserBase):
    """
    Esquema para almacenar un usuario en la base de datos.
    """
    id_person: int = Field(..., description="ID de la persona asociada a este usuario.")
    password: str = Field(..., description="Contraseña hasheada.")

class SchemaItemUser(SchemaUserBase):
    """
    Esquema para representar un usuario en una lista.
    """
    id: int

class SchemaDetailUser(SchemaItemUser):
    """
    Esquema para ver el detalle completo de un usuario (sin contraseña).
    """
    person: SchemaDetailPerson

class SchemaUserUpdate(SchemaUserBase):
    """
    Esquema para actualizar un usuario.
    """
    id: int

    #password: Optional[str] = Field(None, description="Nueva contraseña (opcional).")


class SchemaDetailUserWithPassword(SchemaDetailUser):
    """
    Esquema que representa un usuario con su contraseña hasheada.
    """
    password: str = Field(..., description="Contraseña hasheada del usuario, en formato de texto cifrado.")
