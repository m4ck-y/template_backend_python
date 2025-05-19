from typing import TypeVar, Generic, List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel

from app.utils.infrastructure.database.base_implementation import BaseRepository

# Definimos los tipos genéricos para los modelos
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)  # Esquema de creación
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)  # Esquema de actualización
ReturnSchemaType = TypeVar("ReturnSchemaType", bound=BaseModel)  # Esquema de retorno

class BaseService(Generic[CreateSchemaType, UpdateSchemaType, ReturnSchemaType]):
    def __init__(self, repository: BaseRepository[CreateSchemaType, UpdateSchemaType, ReturnSchemaType]):
        self.repository = repository

    def Create(self, data: CreateSchemaType, db: Session) -> int:
        try:
            return self.repository.Create(data, db)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error de integridad: la entidad ya existe o hay un conflicto en los datos",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ocurrió un error inesperado: {str(e)}",
            )

    def List(self, db: Session) -> List[ReturnSchemaType]:
        try:
            return self.repository.List(db)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ocurrió un error al obtener la lista de entidades: {str(e)}",
            )

    def Get(self, id: int, db: Session) -> Optional[ReturnSchemaType]:
        record = self.repository.Get(id, db)
        if not record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Entidad con ID {id} no encontrada.",
            )
        return record

    def Update(self, data: UpdateSchemaType, db: Session) -> bool:
        try:
            if not self.repository.Update(data, db):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Entidad no encontrada o no actualizada.",
                )
            return True
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error de integridad: no se pudo actualizar la entidad.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ocurrió un error al intentar actualizar la entidad: {str(e)}",
            )

    def Delete(self, id: int, db: Session) -> bool:
        try:
            if not self.repository.Delete(id, db):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Entidad no encontrada o no eliminada.",
                )
            return True
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error de integridad: no se pudo eliminar la entidad.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ocurrió un error al intentar eliminar la entidad: {str(e)}",
            )
