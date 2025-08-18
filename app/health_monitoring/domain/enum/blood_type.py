from enum import Enum

class EBloodType(int, Enum):
    A_POSITIVE = 1#'A+'
    A_NEGATIVE = 2#'A-'
    B_POSITIVE = 3#'B+'
    B_NEGATIVE = 4#'B-'
    AB_POSITIVE = 5#'AB+'
    AB_NEGATIVE = 6#'AB-'
    O_POSITIVE = 7#'O+'
    O_NEGATIVE = 8#'O-'