from datetime import datetime

from model.book import Book
from model.member import Member


class Storage:
    """Reads and writes the data files and the log."""

    def __init__(self, books_file, members_file):
        self.books_file = books_file
        self.members_file = members_file

    def load_books(self):
        """Read the books file and return a list of Book objects."""
        books = []
        with open(self.books_file, "r", encoding="utf-8") as file:
            for line in file:
                fields = line.strip().split(";")
                member_code = fields[5]
                # Un campo vacío significa que el libro está libre
                if member_code == "":
                    member_code = None
                books.append(Book(fields[0], fields[1], fields[2], int(fields[3]), fields[4], member_code))
        return books

    def load_members(self):
        """Read the members file and return a list of Member objects."""
        members = []
        with open(self.members_file, "r", encoding="utf-8") as file:
            for line in file:
                fields = line.strip().split(";")
                book_code = fields[3]
                if book_code == "":
                    book_code = None
                members.append(Member(fields[0], fields[1], fields[2], book_code))
        return members

    def save(self, books, members):
        """Write the books and the members to their files."""
        # "w" borra el contenido anterior y escribe de nuevo
        with open(self.books_file, "w", encoding="utf-8") as file:
            for book in books:
                member_code = book.member_code
                if member_code is None:
                    member_code = ""
                file.write(f"{book.code};{book.title};{book.author};{book.year};{book.category};{member_code}\n")
        with open(self.members_file, "w", encoding="utf-8") as file:
            for member in members:
                book_code = member.book_code
                if book_code is None:
                    book_code = ""
                file.write(f"{member.member_code};{member.name};{member.email};{book_code}\n")

    def write_log(self, event, details):
        """Write a line in log.txt: [date][event][details]."""
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # "a" añade al final del fichero sin borrar lo anterior
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f"[{date}][{event}][{details}]\n")