from enum import Enum

class EOrganizationSize(int, Enum):
    """
    Organization Size

    The size of the organization in terms of employees
    """
    EMPLOYEES_1_10 = 0
    EMPLOYEES_11_50 = 1
    EMPLOYEES_51_200 = 2
    EMPLOYEES_201_500 = 3
    EMPLOYEES_501_1000 = 4
    EMPLOYEES_1001_5000 = 5
    EMPLOYEES_5001_10000 = 6
    EMPLOYEES_10001_OVER = 10