import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()


API_HOST = os.getenv("API_HOST")
API_PORT = int(os.getenv("API_PORT"))

SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DB_URL")

DEBUG = os.getenv("DEBUG", 'false').lower() in ('true', '1', 't')

DB_POSTGRES_HOST = os.getenv("DB_POSTGRES_HOST")
DB_POSTGRES_PORT = os.getenv("DB_POSTGRES_PORT")
DB_POSTGRES_NAME = os.getenv("DB_POSTGRES_NAME")
DB_POSTGRES_USER = os.getenv("DB_POSTGRES_USER")
DB_POSTGRES_PASS = os.getenv("DB_POSTGRES_PASS")