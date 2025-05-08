from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.health.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaUnitCreate as C,
    SchemaUnitUpdate as U,
)
from app.health.application.unit import UnitApplication
from app.config.db import GetSession

router = APIRouter(prefix="/unit", tags=["Unit"])

# Aplicación inyectada desde setup externo (por ejemplo, main.py)
app_layer: UnitApplication = None


def setup_service(application_layer: UnitApplication):
    """
    Configura la capa de aplicación que se utilizará dentro de este router.
    Este patrón permite una fácil inyección de dependencias.
    """


    global app_layer
    app_layer = application_layer

    print("Application layer injected", app_layer)
    return app_layer

@router.post("/", response_model=int)
async def Create(data: C, db: Session = Depends(GetSession)) -> int:
    """
    Create a new unit of measurement.
    """
    return app_layer.Create(data, db)

@router.get("/list", response_model=List[E])
async def List(db: Session = Depends(GetSession)) -> list[E]:
    """
    List all units of measurement.
    """
    return app_layer.List(db)

@router.get("/{id}", response_model=E)
async def Get(id: int, db: Session = Depends(GetSession)) -> E | None:
    """
    Retrieve a unit by its ID.
    """
    return app_layer.Get(id, db)

@router.put("/", response_model=bool)
async def Update(data: U, db: Session = Depends(GetSession)) -> bool:
    """
    Update an existing unit of measurement.
    """
    return app_layer.Update(data, db)

@router.delete("/{id}", response_model=bool)
async def Delete(id: int, db: Session = Depends(GetSession)) -> bool:
    """
    Delete a unit by its ID.
    """
    return app_layer.Delete(id, db)
