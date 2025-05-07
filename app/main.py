from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.config.env import API_HOST, API_PORT
from app.config.init_db import init_db
from app.config.init_api import init_api
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los dominios (no recomendado en producción)
    allow_credentials=True,  # Permite credenciales (cookies, cabeceras de autorización)
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

init_db()
init_api(app) #No registrar dentro de main

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=API_HOST, port=API_PORT, reload=True)