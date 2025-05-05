from app.person.infrastructure.database.init import init as init_person
from app.health.infrastructure.database.init import init as init_health, Seeder as SeederHealth
from app.config.db import Base, engine

def init():

    print("init >>> db ... ") 
    init_person()
    init_health()
    Base.metadata.create_all(bind=engine)
    SeederHealth()

print("app/config/init_db.py")