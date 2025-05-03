from app.person.infrastructure.database.init import init as init_person
from app.config.db import Base, engine

def init():
    init_person()

Base.metadata.create_all(bind=engine)
