from typing import Optional
from pydantic import Field
from app.person.domain.enum.civil_status import ECivilStatus
from app.person.domain.enum.curp_sex import CURPSex
from app.utils.domain.schemas.base_schema import BaseORMModel

class SchemaLegalInfoBase(BaseORMModel):
    type_national_id_sex: CURPSex = Field(..., examples=[CURPSex.HOMBRE])
    type_civil_status: ECivilStatus = Field(..., examples=[ECivilStatus.SOLTERO])
    key_nationality: str = Field(..., examples=["MEX"])

class SchemaCreateAPILegalInfo(SchemaLegalInfoBase):
    pass

class SchemaCreateDBLegalInfo(SchemaLegalInfoBase):
    id_person: int

class SchemaItemLegalInfo(SchemaLegalInfoBase):
    id: int

class SchemaDetailLegalInfo(SchemaItemLegalInfo):
    pass

class SchemaUpdateLegalInfo(BaseORMModel):
    id: int
    type_national_id_sex: Optional[CURPSex] = None
    type_civil_status: Optional[ECivilStatus] = None
    key_nationality: Optional[str] = None
