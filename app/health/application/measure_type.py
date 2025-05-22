from app.utils.application.base import BaseLayerApplication
from app.health.domain.repository.measure_type import IRepositoryMeasureType as IRepository
from app.health.domain.schemas.measure_type import (
    SchemaListItemMeasureType as E,
    SchemaCreateMeasureType as C,
    SchemaUpdateMeasureType as U,
)

class MeasureTypeApplication(BaseLayerApplication[C, U, E]):
    def __init__(self, repository: IRepository):
        super().__init__(repository)