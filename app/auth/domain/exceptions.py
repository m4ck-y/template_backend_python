"""
Excepciones específicas del dominio de autenticación.

Siguiendo los estándares de documentación del proyecto, estas excepciones
proporcionan manejo granular de errores de autenticación y autorización.
"""

from app.utils.domain.exception import DomainException


class AuthenticationException(DomainException):
    """
    Excepción base para errores de autenticación.
    
    Se lanza cuando falla cualquier proceso de autenticación en el sistema,
    proporcionando una base común para todos los errores relacionados.
    """
    pass


class InvalidCredentialsException(AuthenticationException):
    """
    Excepción lanzada cuando las credenciales proporcionadas son incorrectas.
    
    Se utiliza específicamente cuando la contraseña no coincide con la
    almacenada en el sistema para un usuario válido.
    
    Args:
        username (str): **Nombre de usuario** que intentó autenticarse.
                       Se incluye para logging y auditoría de seguridad.
    
    Example:
        >>> raise InvalidCredentialsException("john.doe")
        InvalidCredentialsException: Contraseña incorrecta para usuario: john.doe
    """
    
    def __init__(self, username: str):
        self.username = username
        message = f"Contraseña incorrecta para usuario: {username}"
        super().__init__(message)


class UserNotFoundException(AuthenticationException):
    """
    Excepción lanzada cuando el usuario no existe en el sistema.
    
    Se utiliza cuando se intenta autenticar con un nombre de usuario
    que no está registrado en la base de datos.
    
    Args:
        username (str): **Nombre de usuario** que no fue encontrado.
                       Se incluye para logging y auditoría de seguridad.
    
    Example:
        >>> raise UserNotFoundException("nonexistent.user")
        UserNotFoundException: Usuario no encontrado: nonexistent.user
    """
    
    def __init__(self, username: str):
        self.username = username
        message = f"Usuario no encontrado: {username}"
        super().__init__(message)


class InactiveUserException(AuthenticationException):
    """
    Excepción lanzada cuando el usuario existe pero está inactivo.
    
    Se utiliza cuando un usuario válido intenta autenticarse pero
    su cuenta ha sido desactivada en el sistema.
    
    Args:
        username (str): **Nombre de usuario** que está inactivo.
                       Se incluye para logging y auditoría de seguridad.
    
    Example:
        >>> raise InactiveUserException("inactive.user")
        InactiveUserException: Usuario inactivo: inactive.user
    """
    
    def __init__(self, username: str):
        self.username = username
        message = f"Usuario inactivo: {username}"
        super().__init__(message)