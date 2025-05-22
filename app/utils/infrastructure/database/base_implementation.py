import json
from typing import TypeVar, Generic, Optional, List
from sqlalchemy import and_
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Session
from app.config.db import datetime_now
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel

from app.utils.enum.str_color import StrColor
from app.utils.infrastructure.database.base_model import BaseModel as TableBaseModel
from app.utils.domain.repository.base_repository import IBaseRepository

# Tipos genéricos para los modelos, esquemas y la respuesta
# Representa el modelo de SQLAlchemy
ModelType = TypeVar("ModelType", bound=TableBaseModel)
# Esquema para la creación de entidades
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
# Esquema para la actualización de entidades
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
# Esquema para la respuesta que se devolverá
ReturnSchemaType = TypeVar("ReturnSchemaType", bound=BaseModel)

str_color = StrColor()


class BaseRepository(IBaseRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType, ReturnSchemaType]):
    """
    Clase base para realizar operaciones CRUD estándar en cualquier entidad que herede esta clase.
    """

    def __init__(self, model: ModelType, create_schema: CreateSchemaType, update_schema: UpdateSchemaType, return_schema: ReturnSchemaType, column_list_models: List[any] = []):
        """
        Constructor que inicializa el repositorio con los modelos y esquemas necesarios.

        Args:
            model (ModelType): El modelo de SQLAlchemy que representa la entidad.
            create_schema (CreateSchemaType): Esquema de Pydantic para crear una nueva entidad.
            update_schema (UpdateSchemaType): Esquema de Pydantic para actualizar una entidad existente.
            return_schema (ReturnSchemaType): Esquema de Pydantic para la representación de la entidad en las respuestas.
            column_list_models (Optional[List[any]]): Lista de las **columnas** de relaciones de la entidad que se desean cargar con `joinedload`.


        Example:
        Si tienes un modelo `Person` con relaciones como `list_phones` y `list_addresses`, 
        puedes usar el repositorio base de la siguiente manera:

        ```python
        class PersonRepository(BaseRepository[Table, C, U, E]):
            def __init__(self):
                relationships_to_load = [Table.list_phones, Table.list_addresses]  # Relacionar columnas
                super().__init__(Table, C, U, E, column_list_columns=relationships_to_load)
        
        # Esto permitirá que al hacer `Get` o `List`, las relaciones `list_phones` y `list_addresses` se carguen automáticamente.
        ```

        En el ejemplo anterior:
        - `Table.list_phones` y `Table.list_addresses` son **columnas** del modelo `Person` que representan relaciones 1:N con otras entidades (por ejemplo, `Phone` y `Address`).
        - Estas relaciones se cargarán automáticamente con `joinedload` cuando se obtengan registros de la entidad `Person`.
        """
        self.model = model
        self.create_schema = create_schema
        self.update_schema = update_schema
        self.return_schema = return_schema
        self.column_list_models = column_list_models

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
        print(str_color.RED(">>>> BaseRepository GET"), str_color.YELLOW(self.model.__name__))
        """
        Obtiene una entidad por su ID único.

        Args:
            id (int): ID único de la entidad.
            db (Session): Sesión activa de la base de datos.

        Returns:
            Optional[ReturnSchemaType]: La entidad si se encuentra, o None si no se encuentra.
        """
        # Consulta para obtener la entidad filtrando por ID y asegurando que no esté eliminada

        query = db.query(self.model).filter(and_(self.model.id == id, self.model.deleted_at.is_(None)))


        print(str_color.GREEN("\n>>>> column_list_models"), self.column_list_models)

        for column_list_relation in self.column_list_models:

            query = query.options(
                joinedload(column_list_relation)
            )

        """ record = db.query(self.model).filter(
            self.model.id == id, self.model.deleted_at.is_(None)).first() """
        
        record = query.first()
        #columns of record
        record_structure = json.dumps(record.__dict__, default=str, indent=4)
        print("\t", str_color.MAGENTA(self.model.__name__).YELLOW(" Record Structure: ").RESET(record_structure).CYAN(str(self.return_schema)))
        
        if record:
            # Si la entidad existe, se devuelve utilizando el esquema de respuesta
            return self.return_schema.model_validate(record)
        return None  # Si no se encuentra la entidad, se retorna None

    def List(self, db: Session) -> List[ReturnSchemaType]:

        print(str_color.RED(">>>> BaseRepository LIST"), str_color.YELLOW(self.model.__name__))


        """
        Devuelve una lista de todas las entidades que no han sido eliminadas.

        Args:
            db (Session): Sesión activa de la base de datos.

        Returns:
            List[ReturnSchemaType]: Lista de entidades representadas por el esquema de respuesta.
        """
        # Se obtiene la lista de todas las entidades no eliminadas
        
        records = db.query(self.model).filter(
            self.model.deleted_at.is_(None)).all()
        
        #columns of record
        record_structure = json.dumps(records[0].__dict__, default=str, indent=4)
        print(str_color.GREEN("\t>>>> column_list_models"), self.column_list_models)
        print("\t", str_color.MAGENTA(self.model.__name__).YELLOW(" Record Structure: ").RESET(record_structure).CYAN(str(self.return_schema)))


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
        record = db.query(self.model).filter(
            self.model.id == value.id, self.model.deleted_at.is_(None)).first()
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
        record = db.query(self.model).filter(
            and_(self.model.id == id, self.model.deleted_at.is_(None))).first()
        print(str_color.RED(">>>> Model"), type(self.model), self.model)
        print(str_color.YELLOW(">>>>"), record)
        if not record:
            return False  # Si no se encuentra la entidad, se retorna False
        # Se marca la entidad como eliminada (soft delete) sin borrarla realmente
        record.deleted_at = datetime_now()  # Asigna la fecha de eliminación #
        db.commit()  # Se guarda el cambio en la base de datos
        return True  # Se retorna True indicando que la eliminación fue exitosa
