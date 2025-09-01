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

def verify_token(request: Request, token: str = Depends(oauth2_scheme)):
    """
    Verifica el token. El token puede provenir de dos fuentes:
    1. Cookie 'access_token'
    2. Header 'Authorization'
    
    Si no se encuentra el token en ninguna de estas fuentes, lanza un error.
    """

    token_from_header = token
    token_from_cookie = request.cookies.get("access_token")  # Si el token viene de la cookie

    # Si el token no está en el header, intentamos obtenerlo de la cookie
    if not token_from_header and token_from_cookie:
        token = token_from_cookie
    
    log_info(f"verify_token: {token}, type: {type(token)}")

     # Decodificar el token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            log_info("username is None")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=CREDENTIALS_INVALID_ERROR, headers={"WWW-Authenticate": "Bearer"})
        return payload
    
    except InvalidTokenError as e:
        log_info("InvalidTokenError", e)
        if "expired" in str(e):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=TOKEN_EXPIRED_ERROR)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=TOKEN_INVALID_ERROR)