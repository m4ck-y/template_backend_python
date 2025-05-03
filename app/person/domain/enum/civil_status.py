from enum import Enum

class ECivilStatus(int, Enum):
    SINGLE = 0#"Soltero/a"                 # Nunca ha estado casado
    MARRIED = 1#"Casado/a"                  # Ha adquirido matrimonio civil
    DIVORCED = 2#"Divorciado/a"              # Ha finalizado un matrimonio civil
    SEPARATED = 3#"Separado/a en proceso"    # En trámite de divorcio
    WIDOWED = 4#"Viudo/a"                    # Cónyuge ha fallecido
    COHABITING = 5#"Concubinato"             # Pareja viviendo junta sin matrimonio

#https://www.conceptosjuridicos.com/mx/estado-civil/