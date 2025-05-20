from fastapi import APIRouter, FastAPI, HTTPException, status, Depends
from fastapi.params import Body
from sqlalchemy.orm import Session
from typing import Annotated, TypeVar, Generic, List, Optional, Type, cast # Importa Type
from pydantic import BaseModel
# from app.config.db import GetSession # Asegúrate de que esta importación sea correcta
# from app.utils.application.base import BaseLayerApplication # Asegúrate de que esta importación sea correcta

# --- SIMULACIONES PARA HACER EL CÓDIGO EJECUTABLE ---
# Si tu GetSession y BaseLayerApplication ya están bien definidos,
# puedes ignorar estas simulaciones.
class GetSession:
    def __call__(self):
        # Simula una sesión de base de datos
        class MockSession:
            def __enter__(self): return self
            def __exit__(self, exc_type, exc_val, exc_tb): pass
            def query(self, *args, **kwargs): return self
            def filter(self, *args, **kwargs): return self
            def first(self): return None
            def add(self, *args, **kwargs): pass
            def commit(self): pass
            def refresh(self, *args, **kwargs): pass
            def delete(self, *args, **kwargs): pass
            def all(self): return []
        return MockSession()
# Tipos genéricos para los esquemas
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReturnSchemaType = TypeVar("ReturnSchemaType", bound=BaseModel)

class BaseLayerApplication(Generic[CreateSchemaType, UpdateSchemaType, ReturnSchemaType]):
    def Create(self, data: CreateSchemaType, db: Session) -> int:
        print(f"Application Create: {data.dict()}")
        return 1 # Simula un ID
    def List(self, db: Session) -> List[ReturnSchemaType]:
        print("Application List")
        return []
    def Get(self, id: int, db: Session) -> Optional[ReturnSchemaType]:
        print(f"Application Get: {id}")
        return None
    def Update(self, data: UpdateSchemaType, db: Session) -> bool:
        print(f"Application Update: {data.dict()}")
        return True
    def Delete(self, id: int, db: Session) -> bool:
        print(f"Application Delete: {id}")
        return True
# --- FIN DE SIMULACIONES ---


# Tipos genéricos para los esquemas
# Ahora, TypeVar se enlaza a la clase BaseModel, no a una instancia
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReturnSchemaType = TypeVar("ReturnSchemaType", bound=BaseModel)


class BaseLayerService(Generic[CreateSchemaType, UpdateSchemaType, ReturnSchemaType]):
    """
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
            application_layer: BaseLayerApplication[CreateSchemaType, UpdateSchemaType, ReturnSchemaType],
            # ¡CAMBIO AQUÍ! Esperamos clases de Pydantic, no instancias
            schema_create: Type[CreateSchemaType],
            schema_update: Type[UpdateSchemaType],
            schema_return: Type[ReturnSchemaType],
            route_name: str):

        # Configura el router para el recurso
        self.api_router = APIRouter(prefix=f"/{route_name}", tags=[route_name])
        # Capa de aplicación que maneja operaciones CRUD
        self.application_layer = application_layer
        self.schema_create = schema_create
        self.schema_update = schema_update
        self.schema_return = schema_return
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
        schema_update= self.schema_update
        schema_return = self.schema_return

        print(f"Setting up routes for {self.schema_create.__name__} with route name: {self.api_router.prefix}")

        print(f"schema_create: {schema_create}", type(schema_create))
        print(f"schema_update: {schema_update}", type(schema_update))

        def create_endpoint(data: schema_create, db: Session = Depends(GetSession)) -> int: # type: ignore
            return self.Create(data, db)

        def update_endpoint(data:  schema_update, db: Session = Depends(GetSession)) -> bool:
            return self.Update(data, db)

        # FastAPI infiere el schema del body directamente del tipo del parámetro 'data' en los métodos Create/Update
        self.api_router.post("", response_model=int, status_code=status.HTTP_201_CREATED)(create_endpoint) # Añadido status_code
        self.api_router.get("/list", response_model=List[self.schema_return])(self.List)
        self.api_router.get("/{id}", response_model=self.schema_return)(self.Get)
        self.api_router.put("", response_model=bool)(update_endpoint) # Añadido status_code
        self.api_router.delete("/{id}", response_model=bool)(self.Delete)

        # self.api_router.route # Esta línea no hace nada y puede eliminarse

        # Incluye el router en la API principal
        api_server.include_router(self.api_router)

    # Los métodos Create y Update YA tienen el tipado correcto en sus parámetros:
    # `data: CreateSchemaType` y `data: UpdateSchemaType`.
    # FastAPI usará estos tipos para generar la documentación del cuerpo de la petición.
    def Create(self, data: CreateSchemaType, db: Session = Depends(GetSession)) -> int:
        """
        Crea una nueva entidad en la base de datos.

        Args:
            data: Datos de la entidad a crear.
            db: Sesión de base de datos.

        Returns:
            int: ID de la nueva entidad.
        """
        return self.application_layer.Create(data, db)

    def List(self, db: Session = Depends(GetSession)) -> List[ReturnSchemaType]:
        """
        Lista todas las entidades almacenadas en la base de datos.

        Args:
            db: Sesión de base de datos.

        Returns:
            List: Lista de entidades.
        """
        return self.application_layer.List(db)

    def Get(self, id: int, db: Session = Depends(GetSession)) -> Optional[ReturnSchemaType]:
        """
        Obtiene una entidad por su ID.

        Args:
            id: ID de la entidad a obtener.
            db: Sesión de base de datos.

        Returns:
            Optional: La entidad encontrada, o None si no existe.
        """
        result = self.application_layer.Get(id, db)
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return result

    def Update(self, data: UpdateSchemaType, db: Session = Depends(GetSession)) -> bool:
        """
        Actualiza una entidad existente en la base de datos.

        Args:
            data: Nuevos datos para la entidad.
            db: Sesión de base de datos.

        Returns:
            bool: True si se actualizó correctamente, False si no se encontró la entidad.
        """
        updated = self.application_layer.Update(data, db)
        if not updated:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found or update failed")
        return updated

    def Delete(self, id: int, db: Session = Depends(GetSession)) -> bool:
        """
        Elimina una entidad por su ID.

        Args:
            id: ID de la entidad a eliminar.
            db: Sesión de base de datos.

        Returns:
            bool: True si se eliminó correctamente, False si no se encontró la entidad.
        """
        deleted = self.application_layer.Delete(id, db)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return deleted

# --- EJEMPLO DE USO ---
class UserSchemaBase(BaseModel):
    name: str
    email: str

class UserCreate(UserSchemaBase):
    password: str # Campo adicional para creación

class UserUpdate(BaseModel): # Puede ser un subconjunto o tener campos opcionales
    name: Optional[str] = None
    email: Optional[str] = None

class UserReturn(UserSchemaBase): # El esquema que se devuelve
    id: int
    # No incluir password aquí

# Creamos una instancia de FastAPI
app = FastAPI()

# Creamos una instancia de la capa de aplicación (simulada)
# Asegúrate de pasar el Type, no una instancia
user_application_layer = BaseLayerApplication[UserCreate, UserUpdate, UserReturn]()

# Creamos el servicio/router para los usuarios
user_service = BaseLayerService(
    api_server=app,
    application_layer=user_application_layer,
    schema_create=UserCreate, # ¡Pasa la CLASE!
    schema_update=UserUpdate, # ¡Pasa la CLASE!
    schema_return=UserReturn,
    route_name="users"
)

# Puedes ejecutar esto con `uvicorn your_module_name:app --reload`
# Y luego visitar http://127.0.0.1:8000/docs