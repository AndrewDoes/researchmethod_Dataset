# WindSurf/code13.py

# Constants
BOOK_STATUS_AVAILABLE = "Available"
BOOK_STATUS_BORROWED = "Borrowed"

# Data Structures
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.borrowed = False

    def __str__(self):
        status = BOOK_STATUS_BORROWED if self.borrowed else BOOK_STATUS_AVAILABLE
        return f"{self.title} by {self.author} ({self.year}) - {status}"

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self):
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        year = input("Enter year: ").strip()

        if not year.isdigit():
            print("❌ Invalid year!")
            return

        book = Book(title, author, int(year))
        self.books.append(book)
        print(f"✅ Added '{book.title}' by {book.author} ({book.year}).")

    def view_books(self):
        if not self.books:
            print("📭 No books available.")
            return

        print("\n=== Library Books ===")
        for i, book in enumerate(self.books):
            print(f"{i+1}. {book}")

    def borrow_book(self):
        self.view_books()

        try:
            index = int(input("Enter book number to borrow: ")) - 1

            if index < 0 or index >= len(self.books):
                print("❌ Invalid book number!")
                return

            book = self.books[index]
            if book.borrowed:
                print("❌ This book is already borrowed!")
                return

            book.borrowed = True
            self.borrowed_books.append(book)
            print(f"📖 Borrowed '{book.title}' by {book.author}.")

        #this except is a self add-on after refactoring in order to be able
        #to proceed to analysis
        except ValueError:
            print("❌ Invalid input!")
def library_menu():
    library = Library()

    while True:
        print("\n1. Add Book\n2. View Books\n3. Borrow Book\n4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    library_menu()