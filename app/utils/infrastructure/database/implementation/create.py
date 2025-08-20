
from sqlalchemy.exc import IntegrityError
from app.base.domain.exception import UniqueConstraintException
from app.base.domain.repository.session import TSession
from app.base.domain.schemas.str_schema_json import str_schema_json
from app.base.domain.schemas.create_api import TCreateAPISchema
from app.base.domain.schemas.types import (
    TItemSchema,
    TDetailSchema,
    TUpdateSchema,
)
from app.utils.log import log_error, log_info
from app.base.infrastructure.database.model_type import TModelType

def BaseCreate(model: TModelType, entity: TCreateAPISchema, db: TSession, auto_commit: bool = True) -> int:
    """
    Crea una nueva entidad en la base de datos.
    Args:
        entity (TCreateAPISchema): Datos validados para la nueva entidad.
        db (Session): Sesión activa de SQLAlchemy.
        auto_commit (bool): Si se debe hacer commit de la transacción.
    Returns:
        Optional[int]: ID de la nueva entidad, o None si ocurre un error(como un error de unicidad).
    """
    try:
        # Se crea una nueva instancia del modelo utilizando los datos del esquema
        log_info(str_schema_json(entity))
        new_entity: TModelType = model(**entity.model_dump())
        db.add(new_entity)
        if auto_commit:
            db.commit()
            db.refresh(new_entity)
        else:
            db.flush()
        return new_entity.id
    
    except IntegrityError as e:
        db.rollback()
        log_error(">>>>>>>>>>>>>>>>>>>>>>>>>> No se")
        log_error(e)
        if "unique constraint" in str(e.orig).lower():
            raise UniqueConstraintException(model.__name__, str(e.orig))
        return e
    except Exception as e:
        db.rollback()
        log_error(e)
        return e  # Retorna None si ocurre un error inesperado