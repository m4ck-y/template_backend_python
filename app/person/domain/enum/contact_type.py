from enum import Enum

class EPhoneType(Enum):
    MOBILE = 1#"Celular"

    WORK = 2#"Trabajo"
    HOME = 3#"Casa"
    BUSINESS = 4#"Negocio"

    OTHER = 10#"Otro"

class EAddressType(int, Enum):
    HOME = 1
    WORK = 2
    BUSINESS = 3

    OTHER = 10

class EEmailType(Enum):
    PERSONAL = 2
    
    WORK = 3
    BUSINESS = 4

    OTHER = 10

