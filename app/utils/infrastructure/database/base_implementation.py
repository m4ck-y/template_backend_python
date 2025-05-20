from typing import TypeVar, Generic, Optional, List
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.config.db import datetime_now
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel

from app.utils.enum.str_color import StrColor
from app.utils.infrastructure.database.base_model import BaseModel as TableBaseModel
from app.utils.domain.repository.base_repository import IBaseRepository

# Tipos genéricos para los modelos, esquemas y la respuesta
ModelType = TypeVar("ModelType", bound=TableBaseModel)  # Representa el modelo de SQLAlchemy
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)  # Esquema para la creación de entidades
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)  # Esquema para la actualización de entidades
ReturnSchemaType = TypeVar("ReturnSchemaType", bound=BaseModel)  # Esquema para la respuesta que se devolverá

str_color = StrColor()

class BaseRepository(IBaseRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType, ReturnSchemaType]):
    """
    Clase base para realizar operaciones CRUD estándar en cualquier entidad que herede esta clase.
    """

    def __init__(self, model: ModelType, create_schema: CreateSchemaType, update_schema: UpdateSchemaType, return_schema: ReturnSchemaType):
        """
        Constructor que inicializa el repositorio con los modelos y esquemas necesarios.

        Args:
            model (ModelType): El modelo de SQLAlchemy que representa la entidad.
            create_schema (CreateSchemaType): Esquema de Pydantic para crear una nueva entidad.
            update_schema (UpdateSchemaType): Esquema de Pydantic para actualizar una entidad existente.
            return_schema (ReturnSchemaType): Esquema de Pydantic para la representación de la entidad en las respuestas.
        """
        self.model = model
        self.create_schema = create_schema
        self.update_schema = update_schema
        self.return_schema = return_schema

    def Create(self, entity: CreateSchemaType, db: Session) -> Optional[int]:
        """
        Crea una nueva entidad en la base de datos.

        Args:
            entity (CreateSchemaType): Esquema de entrada para crear la nueva entidad.
            db (Session): Sesión activa de la base de datos.

        Returns:
            int: ID de la nueva entidad creada, o None si ocurre un error (como un error de unicidad).
        """
        try:
            # Se crea una nueva instancia del modelo utilizando los datos del esquema
            new_entity = self.model(**entity.model_dump())
            db.add(new_entity)
            db.commit()
            db.refresh(new_entity)
            return new_entity.id

        except IntegrityError as e:
            # Manejo de excepciones en caso de errores de integridad (por ejemplo, unicidad)
            db.rollback()  # Revertir cambios en caso de error
            print(f"Error de unicidad: {e.orig}")
            return None

    def Get(self, id: int, db: Session) -> Optional[ReturnSchemaType]:
        """
        Obtiene una entidad por su ID único.

        Args:
            id (int): ID único de la entidad.
            db (Session): Sesión activa de la base de datos.

        Returns:
            Optional[ReturnSchemaType]: La entidad si se encuentra, o None si no se encuentra.
        """
        # Consulta para obtener la entidad filtrando por ID y asegurando que no esté eliminada
        record = db.query(self.model).filter(self.model.id == id, self.model.deleted_at.is_(None)).first()
        if record:
            # Si la entidad existe, se devuelve utilizando el esquema de respuesta
            return self.return_schema.model_validate(record)
        return None  # Si no se encuentra la entidad, se retorna None

    def List(self, db: Session) -> List[ReturnSchemaType]:
        """
        Devuelve una lista de todas las entidades que no han sido eliminadas.

        Args:
            db (Session): Sesión activa de la base de datos.

        Returns:
            List[ReturnSchemaType]: Lista de entidades representadas por el esquema de respuesta.
        """
        # Se obtiene la lista de todas las entidades no eliminadas
        records = db.query(self.model).filter(self.model.deleted_at.is_(None)).all()
        # Se transforma cada entidad utilizando el esquema de respuesta
        return [self.return_schema.model_validate(unit) for unit in records]

    def Update(self, value: UpdateSchemaType, db: Session) -> bool:
        """
        Actualiza una entidad existente.

        Args:
            value (UpdateSchemaType): Esquema que contiene los campos a actualizar.
            db (Session): Sesión activa de la base de datos.

        Returns:
            bool: True si la actualización fue exitosa, False si no se encontró la entidad.
        """
        # Se busca la entidad por ID asegurándose de que no haya sido eliminada
        record = db.query(self.model).filter(self.model.id == value.id, self.model.deleted_at.is_(None)).first()
        if not record:
            return False  # Si no se encuentra la entidad, se retorna False
        # Se actualizan los atributos de la entidad con los valores proporcionados
        for k, v in value.model_dump(exclude_unset=True).items():
            setattr(record, k, v)
        db.commit()  # Se guarda la entidad actualizada
        db.refresh(record)  # Se refresca para obtener los cambios recientes
        return True  # Se retorna True indicando que la actualización fue exitosa

    def Delete(self, id: int, db: Session) -> bool:
        """
        Elimina (marcando como eliminada) una entidad por su ID.

        Args:
            id (int): ID de la entidad a eliminar.
            db (Session): Sesión activa de la base de datos.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encontró la entidad.
        """
        # Se busca la entidad por ID asegurándose de que no haya sido eliminada
        record = db.query(self.model).filter(and_(self.model.id == id, self.model.deleted_at.is_(None))).first()
        print(str_color.RED(">>>> Model"), type(self.model), self.model)
        print(str_color.YELLOW(">>>>"), record)
        if not record:
            return False  # Si no se encuentra la entidad, se retorna False
        # Se marca la entidad como eliminada (soft delete) sin borrarla realmente
        record.deleted_at = datetime_now()  # Asigna la fecha de eliminación # 
        db.commit()  # Se guarda el cambio en la base de datos
        return True  # Se retorna True indicando que la eliminación fue exitosa
