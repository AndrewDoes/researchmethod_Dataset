class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self):
        print("\n=== Add Book ===")
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        year = input("Enter year: ").strip()

        if not year.isdigit():
            print("❌ Invalid year!")
            return

        new_book = Book(title, author, year)
        self.books.append(new_book)
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

        try:
            index = int(input("Enter book number to borrow: ")) - 1

            if index < 0 or index >= len(self.books):
                print("❌ Invalid book number!")
                return

            book = self.books[index]
            if book.is_borrowed:
                print("❌ This book is already borrowed!")
                return

            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"📖 Borrowed '{book.title}' by {book.author}.")

        except ValueError:
            print("❌ Invalid input!")

    def return_book(self):
        if not self.borrowed_books:
            print("📭 No borrowed books.")
            return

        print("\n=== Borrowed Books ===")
        for i, book in enumerate(self.borrowed_books, start=1):
            print(f"{i}. {book.title} by {book.author}")

        try:
            index = int(input("Enter book number to return: ")) - 1

            if index < 0 or index >= len(self.borrowed_books):
                print("❌ Invalid book number!")
                return

            returned_book = self.borrowed_books.pop(index)
            returned_book.is_borrowed = False
            print(f"🔄 Returned '{returned_book.title}'.")

        except ValueError:
            print("❌ Invalid input!")

    def library_menu(self):
        while True:
            print("\n1. Add Book\n2. View Books\n3. Borrow Book\n4. Return Book\n5. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.borrow_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice!")


if __name__ == "__main__":
    library = Library()
    library.library_menu()