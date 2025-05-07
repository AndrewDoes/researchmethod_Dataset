from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'year', 'borrowed'])

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year, False))

    def list_books(self):
        return self.books

    def list_borrowed_books(self):
        return self.borrowed_books

    def borrow_book(self, index):
        if 0 <= index < len(self.books):
            book = self.books[index]
            if book.borrowed:
                return False, "❌ This book is already borrowed!"
            self.books[index] = book._replace(borrowed=True)
            self.borrowed_books.append(self.books[index])
            return True, f"📖 Borrowed '{book.title}' by {book.author}."
        return False, "❌ Invalid book number!"

    def return_book(self, index):
        if 0 <= index < len(self.borrowed_books):
            returned_book = self.borrowed_books.pop(index)
            for i, book in enumerate(self.books):
                if (book.title, book.author, book.year) == (returned_book.title, returned_book.author, returned_book.year):
                    self.books[i] = book._replace(borrowed=False)
                    break
            return True, f"🔄 Returned '{returned_book.title}'."
        return False, "❌ Invalid book number!"

def get_valid_input(prompt, validate_fn, error_msg):
    while True:
        value = input(prompt).strip()
        if validate_fn(value):
            return value
        print(error_msg)

def add_book_ui(library):
    print("\n=== Add Book ===")
    title = get_valid_input("Enter book title: ", lambda x: bool(x), "Title cannot be empty!")
    author = get_valid_input("Enter author: ", lambda x: bool(x), "Author cannot be empty!")
    year = get_valid_input("Enter year: ", lambda x: x.isdigit(), "❌ Invalid year!")
    library.add_book(title, author, int(year))
    print(f"✅ Added '{title}' by {author} ({year}).")

def view_books_ui(library):
    books = library.list_books()
    if not books:
        print("📭 No books available.")
        return
    print("\n=== Library Books ===")
    for i, book in enumerate(books, 1):
        status = "Borrowed" if book.borrowed else "Available"
        print(f"{i}. {book.title} by {book.author} ({book.year}) - {status}")

def borrow_book_ui(library):
    books = library.list_books()
    if not books:
        print("📭 No books available.")
        return
    view_books_ui(library)
    try:
        index = int(get_valid_input("Enter book number to borrow: ", lambda x: x.isdigit(), "❌ Invalid input!")) - 1
        success, message = library.borrow_book(index)
        print(message)
    except ValueError:
        print("❌ Invalid input!")

def return_book_ui(library):
    borrowed_books = library.list_borrowed_books()
    if not borrowed_books:
        print("📭 No borrowed books.")
        return
    print("\n=== Borrowed Books ===")
    for i, book in enumerate(borrowed_books, 1):
        print(f"{i}. {book.title} by {book.author}")
    try:
        index = int(get_valid_input("Enter book number to return: ", lambda x: x.isdigit(), "❌ Invalid input!")) - 1
        success, message = library.return_book(index)
        print(message)
    except ValueError:
        print("❌ Invalid input!")

def library_menu():
    library = Library()
    menu_options = {
        "1": ("Add Book", lambda: add_book_ui(library)),
        "2": ("View Books", lambda: view_books_ui(library)),
        "3": ("Borrow Book", lambda: borrow_book_ui(library)),
        "4": ("Return Book", lambda: return_book_ui(library)),
        "5": ("Exit", None)
    }
    while True:
        print("\n" + "\n".join([f"{k}. {v[0]}" for k, v in menu_options.items()]))
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("👋 Exiting...")
            break
        action = menu_options.get(choice)
        if action and action[1]:
            action[1]()
        elif not action:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    library_menu()