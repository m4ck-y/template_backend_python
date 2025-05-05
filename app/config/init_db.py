from app.person.infrastructure.database.init import init as init_person
from app.health.infrastructure.database.init import init as init_health
from app.config.db import Base, engine

def init():
    init_person()
    init_health()

Base.metadata.create_all(bind=engine)
