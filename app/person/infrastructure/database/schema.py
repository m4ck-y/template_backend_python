from app.utils.infrastructure.database.table_name import TableName

NAME = "person"

class PersonSchema:
    NAME = NAME
    TBL_PERSON = TableName(None, "person") #Schema Publico
    TBL_BIRTH = TableName(NAME, "birth")
    TBL_EMAIL = TableName(NAME, "email")
    TBL_PHONE = TableName(NAME, "phone")
    TBL_ADDRESS = TableName(NAME, "address")

    #TODO: analizar estas tablas si quedarian en otro schema

    TBL_DOCUMENT_CATEGORY = TableName(NAME, "document_category")
    TBL_DOCUMENT_IDENTIFIER = TableName(NAME, "document_identifier")
    TBL_IDENTIFIER_TYPE = TableName(NAME, "identifier_type")
    TBL_PERSON_IDENTIFIER = TableName(NAME, "person_identifier")
    TBL_DOCUMENT_TYPE = TableName(NAME, "document_type")
    TBL_DOCUMENT = TableName(NAME, "document")

    TBL_LEGAL_INFO = TableName(NAME, "legal_info")

    TBL_SOCIOCULTURAL_IDENTITY = TableName(NAME, "sociocultural_identity")
