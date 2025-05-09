from datetime import datetime, timezone
from typing import Generator
import pytz

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session as TSession
from sqlalchemy import Column, DateTime, Integer
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


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime_now, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime_now)
    deleted_at = Column(DateTime, nullable=True)
    
    # Campos de auditoría de usuario y su rol o empleado (referencia a `employee_role`)
    #created_by_id_employee_role = Column(Integer, ForeignKey('employee_role.id_employee_role'), nullable=True)  # FK a `employee_role`
    #updated_by_id_employee_role = Column(Integer, ForeignKey('employee_role.id_employee_role'), nullable=True)
    #deleted_by_id_employee_role = Column(Integer, ForeignKey('employee_role.id_employee_role'), nullable=True)

def is_db_postgres():
    return "postgresql" in SQLALCHEMY_DB_URL