from app.utils.application.base import BaseLayerApplication
from app.health_profile.domain.repository.biological_profile import IRepositoryBiologicalProfile as IRepository
from app.health_profile.domain.schemas.biological_profile import (
    SchemaBiologicalProfile as E,
    SchemaCreateBiologicalProfile as C,
    SchemaUpdateBiologicalProfile as U,
)

class BiologicalProfileApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IRepository):
        super().__init__(repository)