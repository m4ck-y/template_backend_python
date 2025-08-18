from app.utils.infrastructure.database.table_name import TableName

NAME = "health_profile"

class HealthProfileSchema:
    NAME = NAME
    TBL_BIOLOGICAL_PROFILE = TableName(NAME, "biological_profile") #TODO: antes era health_info