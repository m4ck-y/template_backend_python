from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.config.env import API_HOST, API_PORT
from app.config.init_db import init
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los dominios (no recomendado en producción)
    allow_credentials=True,  # Permite credenciales (cookies, cabeceras de autorización)
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

init()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=API_HOST, port=API_PORT, reload=True)