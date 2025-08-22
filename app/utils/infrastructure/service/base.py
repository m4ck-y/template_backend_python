from fastapi import APIRouter, FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session # TODO
from typing import  Generic, List, Optional
from app.config.db import GetSession
from app.utils.application.base import BaseLayerApplication
from app.utils.domain.schemas.types import TSchemaItem, TSchemaDetail, TSchemaUpdate, TSchemaCreateAPI
from app.utils.domain.exception import UniqueConstraintException

class BaseLayerService(Generic[TSchemaCreateAPI, TSchemaItem, TSchemaDetail, TSchemaUpdate]):
    """
    **Parámetros genéricos:**
    - `TSchemaCreateAPI`: Tipo que representa el esquema de creación de la entidad (ejemplo: `UserCreate`).
    - `TSchemaItem`: Tipo que representa el esquema de los ítems individuales de la entidad en listados (ejemplo: `UserListItem`).
    - `TSchemaDetail`: Tipo que representa el esquema de la entidad devuelta en detalle (ejemplo: `UserDetail`).
    - `TSchemaUpdate`: Tipo que representa el esquema de actualización de la entidad (ejemplo: `UserUpdate`).

    Capa de servicio genérica para operaciones CRUD y rutas API en FastAPI.

    Esta clase configura las rutas para manejar operaciones de creación, obtención, 
    listado, actualización y eliminación de entidades, delegando la lógica de negocio
    a la capa de aplicación proporcionada. Los métodos CRUD son mapeados a rutas de 
    FastAPI, permitiendo una gestión fácil de los recursos.

    **Atributos:**
    - `api_router`: Router de FastAPI para exponer las rutas del recurso.
    - `application_layer`: Capa que maneja la lógica CRUD.
    - `schema_create`, `schema_update`, `schema_return`: Esquemas utilizados en las operaciones CRUD.
    - `route_name`: Nombre base para las rutas del recurso.

    **Métodos:**
    - `setup_routes`: Configura las rutas CRUD en FastAPI.
    - `create`: Crea una nueva entidad.
    - `list`: Obtiene todas las entidades.
    - `get`: Obtiene una entidad por su ID.
    - `update`: Actualiza una entidad existente.
    - `delete`: Elimina una entidad por su ID.
    """
    def __init__(
            self,
            api_server: FastAPI,
            application_layer: BaseLayerApplication[TSchemaCreateAPI, TSchemaItem, TSchemaDetail, TSchemaUpdate],
            schema_create: TSchemaCreateAPI,
            schema_item: TSchemaItem,
            schema_detail: TSchemaDetail,
            schema_update: TSchemaUpdate, 
            route_name: str, 
            route_parent: str = None):
        

        route_name = f"{route_parent}/{route_name}" if route_parent else route_name

        tags = [route_parent, route_name] if route_parent else [route_name]
        
        # Configura el router para el recurso
        self.api_router = APIRouter(prefix=f"/{route_name}", tags=tags)
        # Capa de aplicación que maneja operaciones CRUD
        self.application_layer: BaseLayerApplication = application_layer
        self.schema_create = schema_create
        self.schema_update = schema_update
        self.schema_item = schema_item  # Esquema para los items en la lista
        self.schema_detail = schema_detail
        self.setup_routes(api_server)

    def setup_routes(self, api_server: FastAPI):
        """
        Configura las rutas CRUD para el recurso en el servidor FastAPI.
        
        **Rutas:** 
        - POST `/`: Crea una nueva entidad.
        - GET `/list`: Lista todas las entidades.
        - GET `/{id}`: Obtiene una entidad por ID.
        - PUT `/`: Actualiza una entidad existente.
        - DELETE `/{id}`: Elimina una entidad por ID.
        """

        schema_create = self.schema_create
        schema_update = self.schema_update

        def Create(data: schema_create, db: Session = Depends(GetSession)) -> int: # type: ignore
            return self.Create(data, db)
        
        def Update(data: schema_update, db: Session = Depends(GetSession)) -> bool: # type: ignore
            return self.Update(data, db)

        self.api_router.post("", response_model=int)(Create)
        self.api_router.get("/list", response_model=List[self.schema_item])(self.List)
        self.api_router.get("/{id}", response_model=self.schema_detail)(self.Get)
        self.api_router.put("", response_model=bool)(Update)
        self.api_router.delete("/{id}", response_model=bool)(self.Delete)

        self.api_router.route

        # Incluye el router en la API principal
        api_server.include_router(self.api_router)

    def Create(self, data: TSchemaCreateAPI, db: Session) -> int:
        """
        Crea una nueva entidad en la base de datos.

        Args:
            data: Datos de la entidad a crear.
            db: Sesión de base de datos.

        Returns:
            int: ID de la nueva entidad.
        """
        try:
            r = self.application_layer.Create(data, db)
            return r
        except UniqueConstraintException as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=str(e.orig)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    def List(self, db: Session = Depends(GetSession)) -> List[TSchemaItem]:
        """
        Lista todas las entidades almacenadas en la base de datos.

        Args:
            db: Sesión de base de datos.

        Returns:
            List: Lista de entidades.
        """
        return self.application_layer.List(db)

    def Get(self, id: int, db: Session = Depends(GetSession)) -> Optional[TSchemaDetail]:
        """
        Obtiene una entidad por su ID.

        Args:
            id: ID de la entidad a obtener.
            db: Sesión de base de datos.

        Returns:
            Optional: La entidad encontrada, o None si no existe.
        """
        r = self.application_layer.Get(id, db)

        if r is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entity not found")
        
        return r

    def Update(self, data: TSchemaUpdate, db: Session) -> bool:
        """
        Actualiza una entidad existente en la base de datos.

        Args:
            data: Nuevos datos para la entidad.
            db: Sesión de base de datos.

        Returns:
            bool: True si se actualizó correctamente, False si no se encontró la entidad.
        """
        r = self.application_layer.Update(data, db)
        if not r:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entity not found")
        return True

    def Delete(self, id: int, db: Session = Depends(GetSession)) -> bool:
        """
        Elimina una entidad por su ID.

        Args:
            id: ID de la entidad a eliminar.
            db: Sesión de base de datos.

        Returns:
            bool: True si se eliminó correctamente, False si no se encontró la entidad.
        """
        r = self.application_layer.Delete(id, db)
        if not r:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entity not found")
        return True
