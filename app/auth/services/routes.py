from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import ValidationError

from app.auth.domain.schemas import SchemaLogin, TokenPayload
from app.auth.domain.exceptions import (
    UserNotFoundException, 
    InvalidCredentialsException, 
    InactiveUserException
)
from app.auth.application.auth import AuthApplication
from app.account.domain.schemas.user import SchemaDetailUser
from app.config.db import GetSession
from app.utils.log import log_info, log_error
from app.utils.jwt import create_access_token

ROUTE_NAME = "auth"

router_auth = APIRouter(
    #prefix="/auth",
    tags=[ROUTE_NAME],
    responses={
        401: {"description": "Credenciales inválidas"},
        404: {"description": "Usuario no encontrado"},
        403: {"description": "Usuario inactivo"}
    }
)

#security = HTTPBearer() TODO: investigar que es esto , y para que sirve

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
    response: Response,
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
        payload = TokenPayload(
            sub=str(user.id),
            username=user.username,
            name=f"{user.person.first_name} {user.person.last_name}",
            url_photo=None
        )

        access_token = create_access_token(payload.to_dict())

        log_info(f"Token generado para usuario {credentials.username}: <type>{type(access_token)}</type> {access_token}")

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            samesite="none", #cuando este el en produccion cambiar a lax
            secure=False #cuando este en el produccion cambiar a True
        )

        return user


        #return user
        
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

# OAuth2PasswordRequestForm es para compatibilidad con Swagger UI OAuth2
@router_auth.post(
    "/token",
    response_model=SchemaDetailUser,
    summary="🎫 Generar token de acceso",
    description="""
Endpoint legacy para compatibilidad con Swagger UI OAuth2.

### ⚠️ Deprecado:
Este endpoint se mantiene por compatibilidad con versiones anteriores.
Se recomienda usar `/auth/login` para nuevas implementaciones.

### 📋 Validaciones de Entrada:
- **Username:** mínimo 3 caracteres, máximo 50
- **Password:** mínimo 6 caracteres, máximo 100

### 🔄 Proceso:
1. Convierte OAuth2PasswordRequestForm a SchemaLogin
2. Valida credenciales con Pydantic
3. Redirige a login_user para autenticación completa
""",
    responses={
        422: {
            "description": "Error de validación en formato estándar FastAPI",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "string_too_short",
                                "loc": ["password"],
                                "msg": "String should have at least 6 characters",
                                "input": "123",
                                "ctx": {"min_length": 6}
                            }
                        ]
                    }
                }
            }
        },
        400: {
            "description": "Error procesando credenciales",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Error procesando las credenciales"
                    }
                }
            }
        }
    },
    deprecated=True
)
def create_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends()
) -> SchemaDetailUser:
    """
    Endpoint legacy para generar token compatible con Swagger UI OAuth2.
    
    Convierte OAuth2PasswordRequestForm a SchemaLogin y redirige a login_user
    para reutilizar toda la lógica de autenticación, manejo de excepciones y
    generación de tokens JWT.
    
    Args:
        form_data (OAuth2PasswordRequestForm): **Formulario OAuth2** con username y password
                                              desde Swagger UI o cliente OAuth2.
        response (Response): **Objeto Response** para configurar cookies JWT.
        
    Returns:
        SchemaDetailUser: Información completa del usuario autenticado sin contraseña.
        
    Raises:
        HTTPException: 422 para errores de validación Pydantic (formato estándar FastAPI),
                      400 para errores de procesamiento,
                      401/403/404/500 propagados desde login_user.
    
    Note:
        Este endpoint mantiene compatibilidad con el flujo OAuth2 de Swagger UI
        mientras reutiliza completamente la lógica de autenticación de /login.
    """
    # Convertir OAuth2PasswordRequestForm a SchemaLogin con validación Pydantic
    try:
        credentials = SchemaLogin(username=form_data.username, password=form_data.password)
    except ValidationError as e:
        log_error(f"Error al parsear credenciales: {str(e)}")
        
        # Convertir ValidationError al formato estándar de FastAPI para máxima compatibilidad
        # Este formato es idéntico al que FastAPI usa internamente para errores 422
        error_details = [
            {
                "type": error['type'],           # Tipo de error (string_too_short, etc.)
                "loc": error['loc'],             # Ubicación del error (campo)
                "msg": error['msg'],             # Mensaje descriptivo
                "input": error.get('input', None),  # Valor que causó el error
                "ctx": error.get('ctx', {})      # Contexto adicional (min_length, etc.)
            }
            for error in e.errors()
        ]
        
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=error_details  # Formato estándar FastAPI para errores de validación
        )
    except Exception as e:
        log_error(f"Error inesperado al parsear credenciales: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error procesando las credenciales"
        )
    
    # Delegar toda la lógica de autenticación a login_user (DRY principle)
    # Esto incluye: validación de usuario, generación JWT, cookies, manejo de excepciones
    return login_user(credentials, response)

#TODO: REFRESH TOKEN
    
from app.utils.jwt import verify_token
@router_auth.get("/verify_token", response_model=dict)
def verify_token(value=Depends(verify_token)):
    """
    Verifica si el token JWT es válido, extraído ya sea de la cookie o del encabezado.
    """
    log_info(f"verify_token: {value}")

    # Asegurarse de que el token esté presente y validado
    if value:
        return JSONResponse(content={"message": "Token is valid"})
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

'''@router_auth.post("/refresh_token", dependencies=[Depends(verify_token)])
def RefreshToken(value: SchemeUserRefreshToken, request: Request):
    """
    Endpoint para renovar el token. Requiere autenticación con un token válido.
    """
    log_info(f"refresh_token: {value}"), type(value)
    #return {"access_token": create_access_token()}


   # Obtener el token de la cookie si no se pasa en el encabezado
    token_from_cookie = request.cookies.get("access_token")
    if token_from_cookie:
        access_token = create_access_token(data=value.to_dict())
        #return {"access_token": access_token} #TODO: DEVOLVER el token en la cookie

    # Si no hay token, lanzar error
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No token found")'''