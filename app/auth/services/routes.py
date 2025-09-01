from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.auth.domain.schemas import SchemaLogin
from app.auth.domain.exceptions import (
    UserNotFoundException, 
    InvalidCredentialsException, 
    InactiveUserException
)
from app.auth.application.auth import AuthApplication
from app.account.domain.schemas.user import SchemaDetailUser
from app.config.db import GetSession
from app.utils.log import log_info, log_error

ROUTE_NAME = "auth"

router_auth = APIRouter(
    prefix="/auth",
    tags=[ROUTE_NAME],
    responses={
        401: {"description": "Credenciales inválidas"},
        404: {"description": "Usuario no encontrado"},
        403: {"description": "Usuario inactivo"}
    }
)

security = HTTPBearer()

__app: AuthApplication = None


def ServiceAuth(api_server: FastAPI, app_layer: AuthApplication):
    """
    Configura el servicio de autenticación en la aplicación FastAPI.
    
    Registra el router de autenticación y configura la capa de aplicación
    para el manejo de operaciones de autenticación.
    
    Args:
        api_server (FastAPI): **Instancia de FastAPI** donde registrar las rutas.
        app_layer (AuthApplication): **Capa de aplicación** para lógica de autenticación.
    """
    global __app
    __app = app_layer
    api_server.include_router(router_auth)


@router_auth.post(
    "/login",
    response_model=SchemaDetailUser,
    summary="🔐 Autenticar usuario",
    description="""
Autentica un usuario con sus credenciales y retorna la información del usuario.

### 🔐 Proceso de Autenticación:
- Valida que el usuario exista en el sistema
- Verifica que el usuario esté activo
- Comprueba que la contraseña sea correcta
- Retorna información completa del usuario (sin contraseña)

### 🛡️ Seguridad:
- Contraseñas hasheadas con bcrypt
- Logging de intentos de autenticación para auditoría
- Manejo granular de errores de autenticación

### 📊 Casos de Uso:
- Login de usuarios en aplicaciones web
- Autenticación para APIs móviles
- Validación de credenciales para sistemas internos
""",
    responses={
        200: {
            "description": "Autenticación exitosa",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "username": "john.doe",
                        "is_active": True,
                        "person": {
                            "id": 1,
                            "first_name": "John",
                            "last_name": "Doe",
                            "type_gender": "MASCULINO"
                        }
                    }
                }
            }
        },
        401: {
            "description": "Contraseña incorrecta",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Contraseña incorrecta para usuario: john.doe"
                    }
                }
            }
        },
        403: {
            "description": "Usuario inactivo",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Usuario inactivo: john.doe"
                    }
                }
            }
        },
        404: {
            "description": "Usuario no encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Usuario no encontrado: nonexistent.user"
                    }
                }
            }
        }
    }
)
def login_user(
    credentials: SchemaLogin, 
    db: Session = Depends(GetSession)
) -> SchemaDetailUser:
    """
    Autentica un usuario con sus credenciales.
    
    Args:
        credentials: Credenciales de login (username y password)
        db: Sesión de base de datos
        
    Returns:
        SchemaDetailUser: Información del usuario autenticado
        
    Raises:
        HTTPException: Error específico según el tipo de fallo de autenticación
    """
    try:
        log_info(f"Intento de autenticación para usuario: {credentials.username}")
        
        user = __app.Login(credentials, db)
        
        log_info(f"Autenticación exitosa para usuario: {credentials.username}")
        return user
        
    except UserNotFoundException as e:
        log_error(f"Usuario no encontrado: {e.username}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
        
    except InvalidCredentialsException as e:
        log_error(f"Credenciales inválidas: {e.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
        
    except InactiveUserException as e:
        log_error(f"Usuario inactivo: {e.username}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e)
        )
        
    except Exception as e:
        log_error(f"Error inesperado en autenticación: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor durante la autenticación"
        )


@router_auth.post(
    "/token",
    response_model=SchemaDetailUser,
    summary="🎫 Generar token de acceso",
    description="""
Endpoint legacy para compatibilidad. Redirige a /auth/login.

### ⚠️ Deprecado:
Este endpoint se mantiene por compatibilidad con versiones anteriores.
Se recomienda usar `/auth/login` para nuevas implementaciones.
""",
    deprecated=True
)
def create_token(
    credentials: SchemaLogin, 
    db: Session = Depends(GetSession)
) -> SchemaDetailUser:
    """
    Endpoint legacy para generar token (redirige a login).
    
    Args:
        credentials: Credenciales de login
        db: Sesión de base de datos
        
    Returns:
        SchemaDetailUser: Información del usuario autenticado
    """
    return login_user(credentials, db)


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Verifica un token de autorización Bearer.
    
    Función auxiliar para validar tokens JWT en endpoints protegidos.
    Actualmente es un placeholder para futura implementación de JWT.
    
    Args:
        credentials: Credenciales Bearer del header Authorization
        
    Returns:
        dict: Información del token validado
        
    Raises:
        HTTPException: Si el token es inválido o ha expirado
        
    Note:
        Esta función requiere implementación de JWT para funcionalidad completa.
    """
    # TODO: Implementar validación JWT cuando se agregue soporte de tokens
    token = credentials.credentials
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autorización requerido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Placeholder para validación JWT
    # En el futuro, aquí se validaría el token JWT y se extraería la información del usuario
    return {"token": token, "valid": True}
    