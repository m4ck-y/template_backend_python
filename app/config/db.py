from datetime import datetime, timezone
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session as SessionDB
from typing import Generator
from sqlalchemy.ext.declarative import declarative_base
from config.env import SQLALCHEMY_DB_URL, DEBUG

print("DEBUG: ", DEBUG)

engine = create_engine(SQLALCHEMY_DB_URL, echo=DEBUG)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def GetSession() -> Generator[SessionDB, None, None]:
    db = Session()
    try:
        yield db
    finally:
        db.close()

def datetime_now(t_zone = timezone.utc) -> datetime:
    
    return datetime.now(t_zone)

Base = declarative_base()