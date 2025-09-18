from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
#from jose import jwt, JWTError
import jwt
from jwt.exceptions import InvalidTokenError
from app.utils.log import log_info

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "liber_salus_sd059854dsd"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DEFAULT_EXPIRE_MINUTES = 15

def timedelta_minutes(minutes: int):
    return timedelta(minutes=minutes)

ACCESS_TOKEN_EXPIRES = timedelta_minutes(ACCESS_TOKEN_EXPIRE_MINUTES)

# Mensajes de error
TOKEN_EXPIRED_ERROR = "Token is expired"
TOKEN_INVALID_ERROR = "Token is invalid"
CREDENTIALS_INVALID_ERROR = "Could not validate credentials"

def create_access_token(data: dict[str, str], expires_delta: timedelta | None = ACCESS_TOKEN_EXPIRES) -> str:
    """
    Crea un token JWT con los datos y la fecha de expiración proporcionada.
    Si no se proporciona una expiración, se usará la predeterminada.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=DEFAULT_EXPIRE_MINUTES)

    log_info(f"Expire time: {expire}")

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def is_valid_token(token: str) -> bool:
    """
    Valida que el token sea realmente válido antes de usarlo.
    
    Verifica que el token:
    - No sea None
    - No sea una cadena vacía
    - No sea "undefined" o "null" (casos típicos de errores en JavaScript)
    - No sea solo espacios
    
    Args:
        token (str): Token a validar
        
    Returns:
        bool: True si el token es válido, False en caso contrario
    """
    if not token:
        return False
    # Solo aplicar lower() para la comparación, no modificar el token original
    token_clean = token.strip().lower()
    return token_clean not in ["", "undefined", "null"]


def verify_token(request: Request, token: str = Depends(oauth2_scheme)):
    """
    Verifica el token. El token puede provenir de dos fuentes:
    1. Header 'Authorization' (prioridad)
    2. Cookie 'access_token' (fallback)
    
    Valida el contenido del token antes de usarlo, no solo su existencia.
    Si no se encuentra un token válido en ninguna fuente, lanza un error.
    """

    token_from_header = token
    token_from_cookie = request.cookies.get("access_token")

    # Limpieza básica (evitar problemas de espacios)
    token_from_header = token_from_header.strip() if token_from_header else None
    token_from_cookie = token_from_cookie.strip() if token_from_cookie else None

    log_info(f"Token from header: {type(token_from_header)} = {token_from_header}")
    log_info(f"Token from cookie: {type(token_from_cookie)} = {token_from_cookie}")

    # Usar el token del header si es válido; si no, usar el de la cookie
    if is_valid_token(token_from_header):
        log_info("TOKEN in header")
        token = token_from_header
    elif is_valid_token(token_from_cookie):
        log_info("TOKEN in cookie")
        token = token_from_cookie
    else:
        log_info("NO token found")
        token = None

    log_info(f"verify_token: {token}, type: {type(token)}")

    # Si no hay token válido, lanzar error inmediatamente
    if not token:
        log_info("No valid token found in header or cookie")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="No valid authentication token found",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Decodificar el token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            log_info("username is None")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=CREDENTIALS_INVALID_ERROR, headers={"WWW-Authenticate": "Bearer"})
        log_info("payload:", payload)
        return payload
    
    except InvalidTokenError as e:
        log_info("InvalidTokenError", e)
        if "expired" in str(e):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=TOKEN_EXPIRED_ERROR)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=TOKEN_INVALID_ERROR)