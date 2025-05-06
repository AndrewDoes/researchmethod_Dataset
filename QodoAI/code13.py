
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({self.year}) - {status}"

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self):
        print("\n=== Add Book ===")
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        year = self.get_valid_input("Enter year: ", int)

        self.books.append(Book(title, author, year))
        print(f"✅ Added '{title}' by {author} ({year}).")

    def view_books(self):
        if not self.books:
            print("📭 No books available.")
            return

        print("\n=== Library Books ===")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def borrow_book(self):
        self.view_books()
        index = self.get_valid_input("Enter book number to borrow: ", int) - 1

        if not (0 <= index < len(self.books)):
            print("❌ Invalid book number!")
            return

        book = self.books[index]
        if book.is_borrowed:
            print("❌ This book is already borrowed!")
            return

        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"📖 Borrowed '{book.title}' by {book.author}.")

    def return_book(self):
        if not self.borrowed_books:
            print("📭 No borrowed books.")
            return

        print("\n=== Borrowed Books ===")
        for i, book in enumerate(self.borrowed_books, start=1):
            print(f"{i}. {book.title} by {book.author}")

        index = self.get_valid_input("Enter book number to return: ", int) - 1

        if not (0 <= index < len(self.borrowed_books)):
            print("❌ Invalid book number!")
            return

        returned_book = self.borrowed_books.pop(index)
        returned_book.is_borrowed = False
        print(f"🔄 Returned '{returned_book.title}'.")

    def library_menu(self):
        actions = {
            "1": self.add_book,
            "2": self.view_books,
            "3": self.borrow_book,
            "4": self.return_book,
            "5": self.exit_program
        }
        while True:
            print("\n1. Add Book\n2. View Books\n3. Borrow Book\n4. Return Book\n5. Exit")
            choice = input("Choose an option: ").strip()
            action = actions.get(choice)
            if action:
                action()
            else:
                print("❌ Invalid choice!")

    def get_valid_input(self, prompt, cast_type):
        while True:
            try:
                return cast_type(input(prompt).strip())
            except ValueError:
                print("❌ Invalid input!")

    def exit_program(self):
        print("👋 Exiting...")
        exit()

if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.library_menu()
