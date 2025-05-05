from app.person.infrastructure.database.model.person import Person
from app.person.infrastructure.database.model.birth_info import BirthInfo
from app.person.infrastructure.database.model.legal_info import LegalInfo
from app.person.infrastructure.database.model.sociocultural_identity import SocioculturalIdentity

#DOCUMENTS
from app.person.infrastructure.database.model.identifier_type import IdentifierType
from app.person.infrastructure.database.model.document_category import DocumentCategory
from app.person.infrastructure.database.model.document_type import DocumentType
from app.person.infrastructure.database.model.document import Document
from app.person.infrastructure.database.model.document_identifier import DocumentIdentifier
from app.person.infrastructure.database.model.person_identifier import PersonIdentifier


#CONTACT INFO

def init():
    print("init >>> person")