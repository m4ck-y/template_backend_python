from enum import Enum
class EBiologicalSex(int, Enum):
    """
    sexoBiologico

    sexoBiologico del paciente,
    es decir la condición biológica y fisiológica de nacimiento.
    
    Se debe registrar una de las siguientes 
    opciones: 
    - 1 – HOMBRE 
    - 2 – MUJER 
    - 3 – INTERSEXUAL

    GIIS-B015-04-11.DATOS DEL PACIENTE
    """
    HOMBRE = 1
    "MALE"
    MUJER = 2
    "FEMALE"
    INTERSEXUAL = 3
    "INTERSEXUAL"