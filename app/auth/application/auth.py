from app.account.domain.repository.user import IRepositoryUser
from app.auth.domain.schemas import SchemaLogin
from app.auth.domain.exceptions import (
    UserNotFoundException, 
    InvalidCredentialsException, 
    InactiveUserException
)
from app.utils.encrypt import verify_password
from app.account.domain.schemas.user import SchemaDetailUser
from app.utils.log import log_info


class AuthApplication:
    """
    Capa de aplicación para operaciones de autenticación.
    
    Implementa la lógica de negocio para autenticación de usuarios,
    incluyendo validación de credenciales y manejo de excepciones específicas.
    """
    
    def __init__(self, user_repo: IRepositoryUser):
        """
        Inicializa la aplicación de autenticación.
        
        Args:
            user_repo (IRepositoryUser): **Repositorio de usuarios** para acceso a datos.
        """
        self.user_repo = user_repo

    def Login(self, value: SchemaLogin, db) -> SchemaDetailUser:
        """
        Autentica un usuario con sus credenciales.
        
        Valida las credenciales del usuario y retorna la información del usuario
        sin la contraseña si la autenticación es exitosa.
        
        Args:
            value (SchemaLogin): **Credenciales de login** (username y password).
            db: **Sesión de base de datos** para consultas.
        
        Returns:
            SchemaDetailUser: Información completa del usuario autenticado sin contraseña.
        
        Raises:
            UserNotFoundException: Si el usuario no existe en el sistema.
            InvalidCredentialsException: Si la contraseña es incorrecta.
            InactiveUserException: Si el usuario existe pero está inactivo.
        
        Example:
            >>> login_data = SchemaLogin(username="john.doe", password="secret123")
            >>> user = auth_app.Login(login_data, db)
            >>> print(user.username)
            "john.doe"
        """
        # Obtener usuario con contraseña desde el repositorio
        user = self.user_repo.GetWithPassword(value.username, db)

        # Validar si el usuario existe
        if user is None:
            log_info(f"Intento de login fallido: Usuario no encontrado - {value.username}")
            raise UserNotFoundException(value.username)

        # Validar si el usuario está activo
        if not user.is_active:
            log_info(f"Intento de login fallido: Usuario inactivo - {value.username}")
            raise InactiveUserException(value.username)

        # Validar contraseña
        if not verify_password(value.password, user.password):
            log_info(f"Intento de login fallido: Contraseña incorrecta - {value.username}")
            raise InvalidCredentialsException(value.username)
        
        # Convertir a esquema sin contraseña
        user_without_password = SchemaDetailUser.model_validate(user)

        log_info(f"Usuario autenticado exitosamente: {user_without_password.username}")

        return user_without_password
        
