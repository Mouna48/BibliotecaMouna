from model.book import Book
from model.member import Member
class storage:
    """Reads and writes the data files and the log"""
    def __init__(self, book_file, members_file) :
        self.book_file = book_file 
        self.members_file = members_file
    def load_books(self) :
        """Read the book file and return a list of book objects"""
        books = []
        with open(self.book_file, "r", encoding="utf-8") as file:
            for line in file:
                fields = line.strip().split(";")
                member_code = fields[5]
                #un campo vacio siginifca que el libro esta libre 
                if member_code == "" :
                    member_code = None
                books.append (book(fields[0]), fields[1], fields [2], int(fields[3]), fields[4], member_code)
        return books
    def load_members(self):
        """Read the member file and return a list of member projects"""
        members = []
        with open(self.members_file, "r", encoding="utf-8") as file:
            for line in file:
                fields = line.strip().split(";")
                book_code = fields[3]
                if book_code == "":
                    book_code = None
                members.append(Member(fields[0], fields[1], fields[2], book_code))
        return members