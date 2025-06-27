from app.person.infrastructure.database.init import init as init_person
from app.health.infrastructure.database.init import init as init_health, Seeder as SeederHealth
from app.company.infrastructure.database.init import init as init_company, Seeder as SeederCompany
from app.config.db import Base, engine, is_db_postgres, CreateSchema

def init_db():

    if is_db_postgres():
        CreateSchema("person", "health", "company")



    print("init >>> db ... ") 
    init_person()
    init_health()
    init_company()
    Base.metadata.create_all(bind=engine)

    SeederHealth()
    SeederCompany()

print("app/config/init_db.py")