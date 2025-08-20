from .business import BusinessValidationException

class DomainException(Exception):
    """Base class for all domain exceptions."""
    pass

class UniqueConstraintException(DomainException):
    """Raised when a unique constraint is violated."""
    def __init__(self, field: str, orig: str = None):
        self.field = field
        text = f"Unique constraint violation on field '{field}'"
        self.orig = orig
        super().__init__(text)