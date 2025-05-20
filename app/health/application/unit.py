from app.utils.application.base import BaseLayerApplication
from app.health.domain.repository.unit import IRepositoryUnit as IRepository
from app.health.domain.schemas.unit import (
    SchemaUnit as E,
    SchemaCreateUnit as C,
    SchemaUpdateUnit as U,
)

class UnitApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IRepository):
        super().__init__(repository)