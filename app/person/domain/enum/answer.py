from enum import Enum

class EAnswerGeneral(int, Enum):
    """
    Se puede registrar una de las siguientes opciones: 
    - 0 – NO 
    - 1 – SI 
    - 2 – NO RESPONDE 
    - 3 – NO SABE 
    Si se desconoce el dato, se debe registrar el valor “-1”. 

    GIIS-B015-04-11.DATOS DEL PACIENTE
    """
    NO = 0
    SI = 1
    NO_RESPONDE = 2
    NO_SABE = 3
    DESCONOCIDO = -1

class EAnswerMigrant(int, Enum):
    """
    Se puede registrar una de las siguientes opciones: 
    - 0 – NO 
    - 1 – NACIONAL 
    - 2 – INTERNACIONAL  
    - 3 – RETORNADO (Sólo nacional) 
    Si se desconoce el dato, se debe registrar el valor “-1”.  

    GIIS-B015-04-11.DATOS DEL PACIENTE
    """
    NO = 0
    NACIONAL = 1
    INTERNACIONAL = 2
    RETORNADO = 3
    DESCONOCIDO = -1