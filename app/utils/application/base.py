from typing import List, TypeVar, Generic, Optional
from app.utils.domain.repository.base_session import TSession
from app.utils.domain.repository.base_repository import IBaseRepository
from pydantic import BaseModel

from app.utils.enum.str_color import StrColor

# Definimos los tipos genéricos para las entidades y esquemas
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReturnSchemaType = TypeVar("ReturnSchemaType", bound=BaseModel)

str_color = StrColor()

class BaseLayerApplication(Generic[CreateSchemaType, UpdateSchemaType, ReturnSchemaType]):
    """

    **Parámetros genéricos:**
    - `CreateSchemaType`: Tipo que representa el esquema de creación de la entidad.
    - `UpdateSchemaType`: Tipo que representa el esquema de actualización de la entidad.
    - `ReturnSchemaType`: Tipo que representa el esquema de la entidad devuelta
      utilizado para devolver datos con formato listo para la presentación.

    Capa de aplicación genérica que maneja operaciones CRUD comunes para cualquier tipo de entidad.
    Las clases específicas de entidad deben heredar de esta clase y proporcionar el repositorio y los esquemas correspondientes.

    Esta clase abstrae las operaciones básicas de creación, lectura, actualización y eliminación (CRUD),
    delegando la lógica de persistencia al repositorio inyectado.
    """

    def __init__(self, repository: IBaseRepository[CreateSchemaType, UpdateSchemaType, ReturnSchemaType]):
        """
        Inicializa la capa de aplicación con un repositorio.

        Args:
            repository: El repositorio que será utilizado para interactuar con la base de datos.
            Este repositorio debe implementar operaciones CRUD genéricas (crear, obtener, listar, actualizar y eliminar).
        """
        self.repository = repository  # El repositorio inyectado que maneja las operaciones de base de datos

        print(
                "\t",
                str_color.CYAN("BaseLayerApplication >>> __init__")\
                .GREEN(", repo:").RESET("\n\t")\
                .YELLOW(str(type(self.repository)))\
                .RESET("\n\t")\
                .RED(str(self.repository)))

    def Create(self, value: CreateSchemaType, db: TSession) -> int:
        """
        Crea una nueva entidad en la base de datos utilizando el repositorio.

        Args:
            value (CreateSchemaType): Los datos de la entidad que se van a crear.
            db (TSession): La sesión activa de la base de datos, que se pasa desde el controlador o el entorno de ejecución.

        Returns:
            ReturnSchemaType: El objeto recién creado, con su ID u otros datos generados por la base de datos.
        """
        return self.repository.Create(value, db)

    def Get(self, id: int, db: TSession) -> Optional[ReturnSchemaType]:
        """
        Obtiene una entidad por su ID desde la base de datos.

        Args:
            id (int): El ID de la entidad que se desea obtener.
            db (TSession): La sesión activa de la base de datos.

        Returns:
            Optional[ReturnSchemaType]: La entidad encontrada, o None si no se encuentra.
        """
        return self.repository.Get(id, db)

    def List(self, db: TSession) -> List[ReturnSchemaType]:
        """
        Obtiene todas las entidades almacenadas en la base de datos.

        Args:
            db (TSession): La sesión activa de la base de datos.

        Returns:
            List[ReturnSchemaType]: Una lista de todas las entidades almacenadas en la base de datos.
        """
        return self.repository.List(db)

    def Update(self, entity: UpdateSchemaType, db: TSession) -> bool:
        """
        Actualiza una entidad existente en la base de datos.

        Args:
            entity (UpdateSchemaType): Los nuevos datos de la entidad que se van a actualizar.
            db (TSession): La sesión activa de la base de datos.

        Returns:
            bool: True si la actualización fue exitosa, False si la entidad no fue encontrada.
        """
        return self.repository.Update(entity, db)

    def Delete(self, id: int, db: TSession) -> bool:
        """
        Elimina una entidad por su ID de la base de datos.

        Args:
            id (int): El ID de la entidad que se desea eliminar.
            db (TSession): La sesión activa de la base de datos.

        Returns:
            bool: True si la entidad fue eliminada correctamente, False si no se encontró.
        """
        print(str_color.MAGENTA("BaseLayerApplication >>> Delete"), ", repo:", type(self.repository), self.repository)
        return self.repository.Delete(id, db)
