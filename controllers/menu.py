from errors.library_errors import LoanError


class Menu:
    """Shows the menu and asks the user for the data of each option."""

    def __init__(self, library):
        self.library = library

    def show_all_books(self):
        """Option 1: show all the books."""
        for book in self.library.books:
            print(book)

    def show_available_books(self):
        """Option 2: show only the free books."""
        for book in self.library.books:
            if book.is_available():
                print(book)

    def search_books(self):
        """Option 3: search books by any word of the title."""
        term = input("Word to search: ")
        books = self.library.search_books(term)
        if len(books) == 0:
            print("No book found")
        for book in books:
            print(book)

    def show_members_with_books(self):
        """Option 6: show the members that have a book and which one."""
        for member in self.library.members:
            if member.has_book():
                book = self.library.find_book(member.book_code)
                print(member.name, "->", book.title)

    def add_book(self):
        """Option 7: add a new book."""
        code = input("Code: ")
        title = input("Title: ")
        author = input("Author: ")
        year = int(input("Year: "))
        category = input("Category: ")
        self.library.add_book(code, title, author, year, category)
        print("Book added")

    def add_member(self):
        """Option 7: add a new member."""
        code = input("Code: ")
        name = input("Name: ")
        email = input("Email: ")
        self.library.add_member(code, name, email)
        print("Member added")

    def save_and_exit(self):
        """Option 8: save the data in the files."""
        self.library.save()
        print("Data saved. Goodbye!")

    def run(self):
        """Repeat the menu until the user chooses option 8."""
        option = ""
        # El menú se repite hasta que el usuario elige la opción 8
        while option != "8":
            print("\n1. Show all books")
            print("2. Show available books")
            print("3. Search a book by title")
            print("4. Lend a book")
            print("5. Return a book")
            print("6. Show members with books")
            print("7. Add a book or a member")
            print("8. Exit")
            option = input("Choose an option: ")
            if option == "1":
                self.show_all_books()
            elif option == "2":
                self.show_available_books()
            elif option == "3":
                self.search_books()
            elif option == "4":
                self.lend_book()
            elif option == "5":
                self.return_book()
            elif option == "6":
                self.show_members_with_books()
            elif option == "7":
                choice = input("1. Add a book  2. Add a member: ")
                if choice == "1":
                    self.add_book()
                else:
                    self.add_member()
            elif option == "8":
                self.save_and_exit()
        def lend_book(self):
        """Option 4: lend a book to a member."""
        book_code = input("Book code: ")
        member_code = input("Member code: ")
        try:
            self.library.lend_book(book_code, member_code)
            print("Book lent")
        except LoanError as e:
            print("Error:", e, "- code:", e.code)

    def return_book(self):
        """Option 5: return the book that a member has."""
        member_code = input("Member code: ")
        try:
            self.library.return_book(member_code)
            print("Book returned")
        except LoanError as e:
            print("Error:", e, "- code:", e.code)