from model.book import Book
from model.member import Member
from controllers.storage import Storage
from errors.library_errors import LoanError


class Library:
    """Manages the books and the members of the library."""

    def __init__(self, books_file, members_file):
        self.storage = Storage(books_file, members_file)
        self.books = self.storage.load_books()
        self.members = self.storage.load_members()
        print("Information loaded:", len(self.books), "books and", len(self.members), "members")

    def find_book(self, code):
        """Return the book with that code, or None."""
        for book in self.books:
            if book.code == code:
                return book
        return None

    def find_member(self, code):
        """Return the member with that code, or None."""
        for member in self.members:
            if member.member_code == code:
                return member
        return None

    def search_books(self, term):
        """Return the books whose title contains the term."""
        result = []
        for book in self.books:
            # lower() pasa a minúsculas para ignorar mayúsculas y minúsculas
            if term.lower() in book.title.lower():
                result.append(book)
        return result

    def add_book(self, code, title, author, year, category):
        """Add a new book to the list."""
        self.books.append(Book(code, title, author, year, category))

    def add_member(self, code, name, email):
        """Add a new member to the list."""
        self.members.append(Member(code, name, email))

    def save(self):
        """Save the current data in the files."""
        self.storage.save(self.books, self.members)