from passlib.context import CryptContext

ALGORITHM = "HS256"

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    """
    Hashea una contraseña utilizando el algoritmo bcrypt.

    Args:
        password (str): Contraseña en texto plano a hashear.

    Returns:
        str: Contraseña hasheada usando bcrypt.

    Detalles técnicos:
        - Utiliza passlib.context.CryptContext con esquema bcrypt
        - Factor de trabajo predeterminado: 12
        - Formato: $2b$12$<22 caracteres de salt><31 caracteres de hash>
        - Salt generado automáticamente para cada hash
    
    Ejemplo:
        >>> hashed = hash_password("MiContraseña123")
        >>> # Resultado similar a:
        >>> # $2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LcdYp/4hkUJZkH8Oa
    """
    return crypt.hash(password)

def verify_password(password:str, hashed_password:str) -> bool:
    return crypt.verify(password, hashed_password)