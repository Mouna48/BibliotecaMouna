class Member:
    """Represents a member of the library."""

    def __init__(self, member_code, name, email, book_code=None):
        self.member_code = member_code
        self.name = name
        self.email = email
        # None significa que el socio no tiene ningún libro prestado
        self.book_code = book_code

    def has_book(self):
        """Return True if the member currently has a borrowed book"""
        return self.book_code is not None
    def __str__(self):
        """Readable text of the member, used by print(member)."""
        status = f"Has book {self.book_code}" if self.has_book() else "No book"
        return f"[{self.member_code}] {self.name} - {self.email} | {status}"