    name = Column(String)
    role = Column(String)
✅ Endpoint adaptado a React Admin:
python
Copiar
Editar
from fastapi import FastAPI, Request, Response, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import asc, desc
from typing import List
import json

from database import get_db  # función que retorna el `Session`
from models import User      # tu modelo SQLAlchemy

app = FastAPI()

# Middleware CORS con headers expuestos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o el dominio de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range"],
)

@app.get("/users")
def list_users(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    sort: str = '["id", "ASC"]',
    range: str = '[0, 9]',
    filter: str = '{}'
):
    sort_field, sort_order = json.loads(sort)
    range_start, range_end = json.loads(range)
    filter_dict = json.loads(filter)

    query = db.query(User)

    # Filtros dinámicos
    for field, value in filter_dict.items():
        query = query.filter(getattr(User, field) == value)

    # Orden
    order = asc(getattr(User, sort_field)) if sort_order == "ASC" else desc(getattr(User, sort_field))
    query = query.order_by(order)

    total = query.count()

    # Paginación
    users = query.offset(range_start).limit(range_end - range_start + 1).all()

    # Headers para React Admin
    response.headers["Content-Range"] = f"users {range_start}-{range_end}/{total}"
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"

    return users