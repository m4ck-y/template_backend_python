from typing import Optional
from datetime import date
from pydantic import Field
from app.utils.domain.schemas.base_schema import BaseORMModel
from app.person.domain.schemas.document_type import SchemaItemDocumentType

class SchemaDocumentBase(BaseORMModel):
    url_file: str = Field(..., examples=["/documents/doc1.pdf"])
    url_thumbnail: Optional[str] = Field(None, examples=["/documents/thumb1.jpg"])
    title: str = Field(..., examples=["Pasaporte Mexicano"])
    description: Optional[str] = Field(None, examples=["Documento de viaje"])
    issued_at: date
    expires_at: date
    verification_status: str = Field(..., examples=["VERIFIED"])
    verified_by: str = Field(..., examples=["SEGOB"])

class SchemaCreateAPIDocument(SchemaDocumentBase):
    id_document_type: int = Field(..., examples=[1])

class SchemaCreateDBDocument(SchemaCreateAPIDocument):
    id_person: int

class SchemaItemDocument(SchemaDocumentBase):
    id: int
    id_document_type: int

class SchemaDetailDocument(SchemaItemDocument):
    document_type: SchemaItemDocumentType

class SchemaUpdateDocument(BaseORMModel):
    id: int
    url_file: Optional[str] = None
    url_thumbnail: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    issued_at: Optional[date] = None
    expires_at: Optional[date] = None
    verification_status: Optional[str] = None
    verified_by: Optional[str] = None
    id_document_type: Optional[int] = None
