import json

from pydantic import BaseModel
from app.utils.domain.schemas.base_schema import BaseORMModel
from app.utils.enum.str_color import StrColor
from app.utils.log import log_error


str_color = StrColor()

def str_schema_json(record_model: BaseORMModel) -> str:
    """
    Genera una representación en texto coloreado del esquema Pydantic recibido.

    Si se pasa una clase Pydantic o una instancia, esta función obtiene el nombre
    de la clase y su estructura interna en formato JSON, aplicando formato de color.

    Args:
        record_model (BaseORMModel): Clase o instancia de un modelo Pydantic.

    Returns:
        str: Cadena con el nombre del esquema en amarillo y su estructura en JSON en azul.
    """

    if isinstance(record_model, type):
        class_name = record_model.__name__
    else:
        class_name = record_model.__class__.__name__
    return str_color\
        .YELLOW(class_name)\
        .BLUE(
            json.dumps(get_model_structure(record_model), indent=4, default=str)
        )


def get_model_structure(model_cls: type[BaseModel]) -> dict:
    """
    Extrae la estructura de campos de un modelo Pydantic, indicando el tipo de cada campo.

    Args:
        model_cls (type[BaseModel]): Clase de un modelo Pydantic.

    Returns:
        dict: Diccionario con los nombres de los campos como claves y los tipos como valores.
              En caso de error, retorna la excepción capturada.
    """
    try:

        return {
            name: field.annotation.__name__
            for name, field in model_cls.model_fields.items()
        }

    except Exception as e:
        log_error(e)
        return e

