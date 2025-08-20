# app/base/domain/exception.py

class BusinessValidationException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
