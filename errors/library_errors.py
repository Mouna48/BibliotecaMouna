class LoanError(Exception):
    """Raised when a book cannot be lent or returned."""

    def __init__(self, code, message):
        # Atributo personalizado: código del libro o del socio que causa el error
        self.code = code
        super().__init__(message)