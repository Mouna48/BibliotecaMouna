from controllers.library import Library
from controllers.menu import Menu

library = Library("data/books.txt", "data/members.txt")
Menu(library).run()