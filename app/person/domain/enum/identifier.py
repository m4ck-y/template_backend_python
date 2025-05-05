from enum import Enum

class EIdentifierType(Enum):
    """
    Enum que describe los diferentes tipos de identificadores para una persona.

    Los posibles valores son:

    * NATIONAL_ID: Identificador único de la persona en México, también conocido como "CURP"
    * FISCAL_ID: Identificador fiscal de la persona en México, también conocido como "RFC"
    * SOCIAL_SECURITY_ID: Identificador de la persona en el sistema de seguridad social de México, también conocido como "NSS"
    """

    NATIONAL_ID = "NATIONAL_ID"
    """Identificador único de la persona en México, también conocido como "CURP"."""

    FISCAL_ID = "FISCAL_ID"
    """Identificador fiscal de la persona en México, también conocido como "RFC"."""

    SOCIAL_SECURITY_ID = "SOCIAL_SECURITY_ID"
    """Identificador de la persona en el sistema de seguridad social de México, también conocido como "NSS"."""
