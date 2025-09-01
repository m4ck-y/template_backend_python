"""
Schemas del dominio de autenticación.

Define las estructuras de datos utilizadas para operaciones de autenticación
y autorización en el sistema, siguiendo los estándares de Pydantic v2.
"""
from dataclasses import dataclass, asdict
from pydantic import BaseModel, Field
from typing import Optional


@dataclass
class TokenPayload:
    sub: str
    username: str
    name: str
    url_photo: Optional[str]

    # Método para convertir la instancia a un diccionario
    def to_dict(self) -> dict[str, str]:
        return asdict(self)


class SchemaLogin(BaseModel):
    """
    Schema para credenciales de autenticación de usuario.
    
    Representa las credenciales básicas requeridas para autenticar
    un usuario en el sistema mediante username y password.
    
    Attributes:
        username (str): **Nombre de usuario** único en el sistema.
                       Debe corresponder a un usuario registrado.
        password (str): **Contraseña en texto plano** del usuario.
                       Se validará contra la contraseña hasheada almacenada.
    """
    
    username: str = Field(
        ..., 
        min_length=3,
        max_length=50,
        description="Nombre de usuario único en el sistema",
        examples=["john.doe", "maria.garcia", "admin"]
    )
    
    password: str = Field(
        ..., 
        min_length=6,
        max_length=100,
        description="Contraseña del usuario en texto plano",
        examples=["mi_password_123", "contraseña_segura"]
    )


class SchemaTokenResponse(BaseModel):
    """
    Schema para respuesta de token de autenticación.
    
    Representa la respuesta del sistema cuando se genera un token
    de acceso exitosamente tras la autenticación.
    
    Attributes:
        access_token (str): **Token de acceso** JWT generado.
        token_type (str): **Tipo de token** (siempre "bearer").
        expires_in (Optional[int]): **Tiempo de expiración** en segundos.
    
    Note:
        Este schema está preparado para futura implementación de JWT.
    """
    
    access_token: str = Field(
        ...,
        description="Token JWT de acceso al sistema",
        examples=["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."]
    )
    
    token_type: str = Field(
        default="bearer",
        description="Tipo de token de autorización",
        examples=["bearer"]
    )
    
    expires_in: Optional[int] = Field(
        default=3600,
        description="Tiempo de expiración del token en segundos",
        examples=[3600, 7200]
    )

    class Config:
        """Configuración del schema."""
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "expires_in": 3600
            }
        }