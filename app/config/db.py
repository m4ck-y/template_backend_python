from datetime import datetime, timezone
from typing import Generator
import pytz

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session as TSession
from sqlalchemy.ext.declarative import declarative_base

from app.config.env import SQLALCHEMY_DB_URL, DEBUG

print("DEBUG: ", DEBUG)

engine = create_engine(SQLALCHEMY_DB_URL, echo=DEBUG)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def GetSession() -> Generator[TSession, None, None]:
    db = Session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()

def datetime_now(t_zone=timezone.utc) -> datetime:
    if "postgresql" in SQLALCHEMY_DB_URL:
        return datetime.now(t_zone)
    return datetime.now(t_zone).astimezone(pytz.utc)

Base = declarative_base()

def is_db_postgres():
    return "postgresql" in SQLALCHEMY_DB_URL