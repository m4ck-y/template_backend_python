from enum import Enum

class EGenderIdentity(Enum):
    """
    Identidad de género del paciente o atributos sociales aprendidos o adoptados por la persona.

    Se debe registrar una de las siguientes opciones: 
    - 0 – NO ESPECIFICADO 
    - 1 – MASCULINO 
    - 2 – FEMENINO 
    - 3 – TRANSGÉNERO 
    - 4 – TRANSEXUAL 
    - 5 – TRAVESTI 
    - 6 – INTERSEXUAL 
    - 88 – OTRO

    GIIS-B015-04-11.DATOS DEL PACIENTE
    """

    NO_ESPECIFICADO = 0
    "NOT_SPECIFIED"

    MASCULINO = 1
    "MALE"

    FEMENINO = 2
    "FEMALE"

    TRANSGENERO = 3
    "TRANSGENDER"

    TRANSEXUAL = 4
    "TRANSSEXUAL"

    TRAVESTI = 5
    "TRANSVESTITE"

    INTERSEXUAL = 6
    "INTERSEXUAL"

    OTRO = 88
    "OTHER"