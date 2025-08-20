from app.utils.domain.schemas.basemodel import ORMModel
from app.person.domain.enum.contact_type import EEmailType
from pydantic import EmailStr

class SchemaBaseEmail(ORMModel):
    type_email: EEmailType
    email: EmailStr

class SchemaCreateAPIEmail(SchemaBaseEmail):
    id_person: int

class SchemaCreateDBEmail(SchemaBaseEmail):
    id_person: int

class SchemaItemEmail(SchemaBaseEmail):
    id: int
    id_person: int

class SchemaDetailEmail(SchemaBaseEmail):
    id: int
    id_person: int