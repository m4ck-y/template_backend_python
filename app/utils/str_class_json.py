import json
from app.utils.enum.str_color import StrColor

str_color = StrColor()

def str_class_json(obj: object) -> str:
    class_name = obj.__class__.__name__
    
    try:
        # Intentar usar __dict__ si es un objeto normal
        data = obj.__dict__
    except AttributeError:
        # Si no tiene __dict__, usar el objeto directamente (e.g., namedtuple o dataclass frozen)
        data = obj

    return str_color.MAGENTA(class_name).CYAN(
        json.dumps(data, default=str, indent=4)
    )