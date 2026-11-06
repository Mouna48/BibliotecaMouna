from model.book import book
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