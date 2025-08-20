import json
from typing import Generic, Optional, List
from sqlalchemy import and_
from sqlalchemy.orm import joinedload, Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, OperationalError
from pydantic import BaseModel

from app.utils.domain.schemas.str_schema_json import str_schema_json
from app.utils.infrastructure.database.implementation.create import BaseCreate
from app.utils.infrastructure.database.models.str_model_json import str_record_model_json
from app.config.db import datetime_now
from app.utils.enum.str_color import StrColor
from app.utils.domain.repository.base_repository import IBaseRepository
from app.utils.domain.schemas.types import (
    TSchemaCreateAPI,
    TSchemaItem,
    TSchemaDetail,
    TSchemaUpdate,
)
from app.utils.infrastructure.database.models.model_type import TModelType
from app.utils.domain.exception import UniqueConstraintException
from app.utils.log import log_error, log_info

str_color = StrColor()


class BaseRepository(IBaseRepository, Generic[TModelType, TSchemaCreateAPI, TSchemaItem, TSchemaDetail, TSchemaUpdate]):
    """
    **Parámetros genéricos:**
    - `TModelType`: Tipo que representa el Modelo de SQLAlchemy que representa la tabla de la base de datos.
    - `TCreateAPISchema`: Tipo que representa el esquema de creación de la entidad (ejemplo: `UserCreate`).
    - `TItemSchema`: Tipo que representa el esquema de los ítems individuales de la entidad en listados (ejemplo: `UserListItem`).
    - `TDetailSchema`: Tipo que representa el esquema de la entidad devuelta en detalle (ejemplo: `UserDetail`).
    - `TUpdateSchema`: Tipo que representa el esquema de actualización de la entidad (ejemplo: `UserUpdate`).

    Implementación base del patrón de repositorio para realizar operaciones CRUD estándar.
    Esta clase utiliza SQLAlchemy y Pydantic para mapear entre modelos de base de datos y esquemas.
    Permite definir una sola vez la lógica genérica de persistencia para cualquier entidad del dominio.

    Notas:
    - Aplica `joinedload` opcionalmente a relaciones indicadas mediante `column_list_models`.
    - Usa borrado lógico a través del campo `deleted_at`.
    """

    def __init__(
        self,
        model: TModelType,
        create_schema: TSchemaCreateAPI,
        item_schema: TSchemaItem,
        detail_schema: TSchemaDetail,
        update_schema: TSchemaUpdate,
        column_list_models: List[any] = [],
    ):
        """
        Inicializa una instancia del repositorio base con los modelos y esquemas necesarios.

        Esta clase permite centralizar y reutilizar la lógica CRUD común para cualquier entidad.
        Se apoya en SQLAlchemy para la interacción con la base de datos y en Pydantic para validación
        y serialización de datos de entrada y salida.

        Args:
            model (TModelType): Modelo de SQLAlchemy que representa la tabla de la base de datos.
            create_schema (TSchemaCreateAPI): Esquema de entrada para crear una nueva instancia de entidad.
            item_schema (TSchemaItem): Esquema para representar entidades en listados (resumen).
            detail_schema (TSchemaDetail): Esquema de salida detallado, utilizado por ejemplo en `Get`.
            update_schema (TSchemaUpdate): Esquema de entrada para actualizar una instancia existente.
            column_list_models (Optional[List[Any]]): Lista de relaciones (columnas) que se deben cargar
                automáticamente al consultar (`joinedload`), útil para evitar consultas perezosas.

        Ejemplo de uso:
        ----------------
        Supongamos que tienes un modelo `Person` con relaciones `phones` y `addresses`.
        Puedes extender esta clase para crear un repositorio específico así:

        ```python
        class PersonRepository(BaseRepository[PersonModel, PersonCreate, PersonListItem, PersonDetail, PersonUpdate]):
            def __init__(self):
                super().__init__(
                    model=PersonModel,
                    create_schema=PersonCreate,
                    item_schema=PersonListItem,
                    detail_schema=PersonDetail,
                    update_schema=PersonUpdate,
                    column_list_models=[PersonModel.phones, PersonModel.addresses]
                )
        ```

        En este ejemplo:
        - `phones` y `addresses` son atributos relacionados del modelo `Person`.
        - Al hacer un `Get` o `List`, estas relaciones serán cargadas automáticamente usando `joinedload`,
          evitando múltiples consultas a la base de datos (n+1 problem).

        """
        self.model = model
        self.create_schema = create_schema
        self.item_schema = item_schema
        self.detail_schema = detail_schema
        self.update_schema = update_schema
        self.column_list_models = column_list_models

    def Create(self, entity: TSchemaCreateAPI, db: Session, auto_commit: bool = True) -> Optional[int]:
        """
        Crea una nueva entidad en la base de datos.

        Args:
            entity (TSchemaCreateAPI): Datos validados para la nueva entidad.
            db (Session): Sesión activa de SQLAlchemy.
            auto_commit (bool): Si se debe hacer commit de la transacción.

        Returns:
            Optional[int]: ID de la nueva entidad, o None si ocurre un error(como un error de unicidad).
        """
        return BaseCreate(self.model, entity, db, auto_commit)

    def Get(self, id: int, db: Session) -> Optional[TSchemaDetail]:
        print(str_color.RED(">>>> BaseRepository GET"), str_color.YELLOW(self.model.__name__))
        """
        Obtiene una entidad por su ID, incluyendo relaciones si se especificaron.

        Args:
            id (int): ID único de la entidad.
            db (Session): Sesión activa de SQLAlchemy.

        Returns:
            Optional[TSchemaDetail]: Instancia del esquema de detalle o None si no existe.
        """
        # Consulta para obtener la entidad filtrando por ID y asegurando que no esté eliminada

        query = db.query(self.model).filter(and_(self.model.id == id, self.model.deleted_at.is_(None)))


        print(str_color.GREEN("\n>>>> column_list_models"), self.column_list_models)

        for column_list_relation in self.column_list_models:

            query = query.options(
                #joinedload(column_list_relation)
                column_list_relation
            )

        """ record = db.query(self.model).filter(
            self.model.id == id, self.model.deleted_at.is_(None)).first() """
        
        record = query.first()

        print(str_color.YELLOW(">>>> Record"), record)
        
        if record:
            print(str_color.GREEN(">>>> Record Found"), record)
            # Si la entidad existe, se devuelve utilizando el esquema de respuesta

            log_info(str_record_model_json(record))
            
            log_info(str_schema_json(self.detail_schema))
        
            return self.detail_schema.model_validate(record, from_attributes=True)
        
        print(str_color.RED(">>>> Record Not Found"))
        return None  # Si no se encuentra la entidad, se retorna None

    def List(self, db: Session) -> List[TSchemaItem]:

        """
        Devuelve una lista de entidades activas (no eliminadas), usando el esquema de ítems.

        Args:
            db (Session): Sesión activa de SQLAlchemy.

        Returns:
            List[TSchemaItem]: Lista de esquemas representando entidades activas.
        """

        print(str_color.RED(">>>> BaseRepository LIST"), str_color.YELLOW(self.model.__name__))
        # Se obtiene la lista de todas las entidades no eliminadas
        
        records = db.query(self.model).filter(
            self.model.deleted_at.is_(None)).all()
        
        #columns of record
        if len(records) > 0:
            record_structure = json.dumps(records[0].__dict__, default=str, indent=4)
            print(str_color.GREEN("\t>>>> column_list_models"), self.column_list_models)
            print("\t", str_color.MAGENTA(self.model.__name__).YELLOW(" Record Structure: ").RESET(record_structure).CYAN(str(self.item_schema)))


        # Se transforma cada entidad utilizando el esquema de respuesta
        return [self.item_schema.model_validate(unit) for unit in records]

    def Update(self, value: TSchemaUpdate, db: Session, auto_commit: bool = True) -> bool:
        """
        Actualiza una entidad existente en la base de datos.

        Args:
            value (TSchemaUpdate): Esquema con los campos a modificar.
            db (Session): Sesión activa de SQLAlchemy.
            auto_commit (bool): Si se debe hacer commit de la transacción.

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
        if auto_commit:
            db.commit()  # Se guarda la entidad actualizada
            db.refresh(record)  # Se refresca para obtener los cambios recientes
        else:
            db.flush()
        return True  # Se retorna True indicando que la actualización fue exitosa

    def Delete(self, id: int, db: Session, auto_commit: bool = True) -> bool:
        """
        Elimina (marcando como eliminada) una entidad por su ID.

        Args:
            id (int): ID de la entidad a eliminar.
            db (Session): Sesión activa de la base de datos.
            auto_commit (bool): Si se debe hacer commit de la transacción.

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
        if auto_commit:
            db.commit()  # Se guarda el cambio en la base de datos
        else:
            db.flush()
        return True  # Se retorna True indicando que la eliminación fue exitosa
