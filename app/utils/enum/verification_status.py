import enum
class EVerificationStatus(enum.Enum):
    """
    - REJECTED  Rechazado
    - PENDING   Pendiente
    - APPROVED  Aprobado
    """

    "Rechazado"
    REJECTED = "REJECTED"

    "Pendiente"
    PENDING = "PENDING"

    "Aprobado"
    APPROVED = "APPROVED"