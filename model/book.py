class book:
    """Represents a book in the library."""
    def __init__(self, code, title, author, year, category, member_code=None):
        self.code = code
        self.title = title 
        self.author = author
        self.year = year
        self.category = category
        # None significa que el libro esta libre y no esta prestado
        self.member_code = member_code
    def is_available(self):
        """Return true if the book is not borrowed by any member"""
        return self.member_code is None
    def __str__(self):
        """Readable text of the book, used by print(book)."""
        status = "Available" if self.is_available() else f"Borrowed by member {self.member_code}"
        return f"[{self.code}] {self.title} - {self.author} ({self.year}) | {status}"
    