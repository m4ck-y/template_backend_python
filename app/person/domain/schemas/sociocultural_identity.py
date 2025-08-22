from typing import Optional
from pydantic import Field
from app.person.domain.enum.answer import EAnswerGeneral, EAnswerMigrant
from app.utils.domain.schemas.base_schema import BaseORMModel

class SchemaSocioculturalIdentityBase(BaseORMModel):
    self_considers_indigenous: EAnswerGeneral = Field(..., examples=[EAnswerGeneral.SI])
    key_indigenous_language: Optional[str] = Field(None, examples=["nahuatl"])
    self_considers_migrant: EAnswerMigrant = Field(..., examples=[EAnswerMigrant.NO])
    key_country_origin: Optional[str] = Field(None, examples=["GTM"])
    key_religion: Optional[str] = Field(None, examples=["110101"])

class SchemaCreateAPISocioculturalIdentity(SchemaSocioculturalIdentityBase):
    pass

class SchemaCreateDBSocioculturalIdentity(SchemaSocioculturalIdentityBase):
    id_person: int

class SchemaItemSocioculturalIdentity(SchemaSocioculturalIdentityBase):
    id: int

class SchemaDetailSocioculturalIdentity(SchemaItemSocioculturalIdentity):
    pass

class SchemaUpdateSocioculturalIdentity(BaseORMModel):
    id: int
    self_considers_indigenous: Optional[EAnswerGeneral] = None
    key_indigenous_language: Optional[str] = None
    self_considers_migrant: Optional[EAnswerMigrant] = None
    key_country_origin: Optional[str] = None
    key_religion: Optional[str] = None
