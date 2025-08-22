from app.utils.infrastructure.database.table_name import TableName

NAME = "account"

class AccountSchema:
    NAME = NAME
    TBL_USER = TableName(NAME, "user")
