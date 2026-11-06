class BookNotAvailableError(Exception):
    """Raised when trying to lend a book that is already borrowed."""

    def __init__(self, book_code, message="The book is not available"):
        # Atributo personalizado: código del libro que ha causado el error
        self.book_code = book_code
        super().__init__(f"{message}: {book_code}")


class MemberAlreadyHasBookError(Exception):
    """Raised when a member tries to borrow a book but already has one."""

    def __init__(self, member_code, message="The member already has a book"):
        # Atributo personalizado: código del socio que ya tiene un libro
        self.member_code = member_code
        super().__init__(f"{message}: {member_code}")
        