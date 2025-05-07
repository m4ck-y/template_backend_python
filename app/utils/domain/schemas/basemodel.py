from pydantic import BaseModel, ConfigDict

class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Se usa ConfigDict en lugar de la clase Config