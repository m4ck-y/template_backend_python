from datetime import datetime, timezone
from typing import Generator
import pytz

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session as SessionDB
from sqlalchemy.ext.declarative import declarative_base

from app.config.env import SQLALCHEMY_DB_URL, DEBUG

print("DEBUG: ", DEBUG)

engine = create_engine(SQLALCHEMY_DB_URL, echo=DEBUG)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def GetSession() -> Generator[SessionDB, None, None]:
    db = Session()
    try:
        yield db
    finally:
        db.close()

def datetime_now(t_zone=timezone.utc) -> datetime:
    if "postgresql" in SQLALCHEMY_DB_URL:
        return datetime.now(t_zone)
    return datetime.now(t_zone).astimezone(pytz.utc)

Base = declarative_base()

def is_db_postgres():
    return "postgresql" in SQLALCHEMY_DB_URL

# Clase base abstracta para modelos dentro del esquema 'public'
class PublicBase(Base):
    __abstract__ = True

    @classmethod
    def __tablename__(cls):
        # En PostgreSQL usa solo el nombre de la clase (la tabla se ubicará en el schema 'public')
        # En SQLite antepone 'public_' para simular el esquema
        return cls.__name__.lower() if is_db_postgres() else f"public_{cls.__name__.lower()}"

    # Solo en PostgreSQL se especifica el esquema
    __table_args__ = {'schema': 'public'} if is_db_postgres() else {}
