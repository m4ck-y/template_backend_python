from app.person.infrastructure.database.init import init as init_person
from app.health.infrastructure.database.init import init as init_health, Seeder as SeederHealth
from app.company.infrastructure.database.init import init as init_company, Seeder as SeederCompany
from app.health_facility.infrastructure.database.init import init as init_health_facility, Seeder as SeederHealthFacility
from app.account.infrastructure.database.init import init as init_account

from app.config.db import Base, engine, is_db_postgres, CreateSchema

def init_db():

    if is_db_postgres():
        CreateSchema("person", "health", "company", "health_facility", "account", "security", "profile")



    print("init >>> db ... ") 
    init_person()
    init_health()
    init_company()
    init_health_facility()
    init_account()
    Base.metadata.create_all(bind=engine)

    SeederHealth()
    id_health_industry = SeederCompany()

    SeederHealthFacility(id_health_industry)

print("app/config/init_db.py")