class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self) -> None:
        self.books = []
        self.borrowed_books = []

    def add_book(self) -> None:
        print("\n=== Add Book ===")
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        year = self._get_valid_year("Enter year: ")

        if year is not None:
            self.books.append(Book(title, author, year))
            print(f"✅ Added '{title}' by {author} ({year}).")

    def view_books(self) -> None:
        if not self.books:
            print("📭 No books available.")
            return

        print("\n=== Library Books ===")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def borrow_book(self) -> None:
        self.view_books()
        index = self._get_valid_index("Enter book number to borrow: ", self.books)

        if index is not None:
            book = self.books[index]
            if book.is_borrowed:
                print("❌ This book is already borrowed!")
            else:
                book.is_borrowed = True
                self.borrowed_books.append(book)
                print(f"📖 Borrowed '{book.title}' by {book.author}.")

    def return_book(self) -> None:
        if not self.borrowed_books:
            print("📭 No borrowed books.")
            return

        print("\n=== Borrowed Books ===")
        for i, book in enumerate(self.borrowed_books, start=1):
            print(f"{i}. {book.title} by {book.author}")

        index = self._get_valid_index("Enter book number to return: ", self.borrowed_books)

        if index is not None:
            book = self.borrowed_books.pop(index)
            book.is_borrowed = False
            print(f"🔄 Returned '{book.title}'.")

    def library_menu(self) -> None:
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

    def exit_program(self) -> None:
        print("👋 Exiting...")
        exit()

    @staticmethod
    def _get_valid_year(prompt: str) -> int:
        try:
            year = int(input(prompt).strip())
            return year
        except ValueError:
            print("❌ Invalid year!")
            return None

    @staticmethod
    def _get_valid_index(prompt: str, collection: list) -> int:
        try:
            index = int(input(prompt).strip()) - 1
            if 0 <= index < len(collection):
                return index
            else:
                print("❌ Invalid book number!")
        except ValueError:
            print("❌ Invalid input!")
        return None


if __name__ == "__main__":
    library = Library()
    library.library_menu()