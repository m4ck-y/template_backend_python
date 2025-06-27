from enum import Enum

class EOrganizationType(Enum):
    """
    Enum que define los diferentes tipos de organizaciones.

    Esta enumeración contiene los tipos de organizaciones más comunes, 
    representados por valores numéricos y una descripción de cada tipo.

    Los tipos de organización incluyen:
    - PUBLIC_COMPANY: Empresa pública (valor: 0)
    - SELF_EMPLOYED: Trabajador autónomo (valor: 1)
    - GOVERNMENT_AGENCY: Agencia gubernamental (valor: 2)
    - NONPROFIT_ORGANIZATION: Organización sin fines de lucro (valor: 3)
    - SOLE_PROPRIETORSHIP: Propiedad única (valor: 4)
    - PRIVATELY_HELD: Empresa de capital privado (valor: 5)
    - PARTNERSHIP: Sociedad de responsabilidad limitada (valor: 6)
    """
    PUBLIC_COMPANY = 0
    "Empresa pública"
    SELF_EMPLOYED = 1
    "Trabajador autónomo"
    GOVERNMENT_AGENCY = 2
    "Agencia gubernamental"
    NONPROFIT_ORGANIZATION = 3
    "Organización sin fines de lucro"
    SOLE_PROPRIETORSHIP = 4
    "Propiedad única"
    PRIVATELY_HELD = 5
    "Empresa de capital privado"
    PARTNERSHIP = 6
    "Sociedad de responsabilidad limitada"