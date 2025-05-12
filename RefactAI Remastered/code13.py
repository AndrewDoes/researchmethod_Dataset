from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    title: str
    author: str
    year: int
    borrowed: bool = False

class LibrarySystem:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self):
        print("\n=== Add Book ===")
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        year = input("Enter year: ").strip()

        if not year.isdigit():
            print("❌ Invalid year!")
            return

        self.books.append(Book(title, author, int(year)))
        print(f"✅ Added '{title}' by {author} ({year}).")

    def view_books(self):
        if not self.books:
            print("📭 No books available.")
            return

        print("\n=== Library Books ===")
        for i, book in enumerate(self.books, 1):
            status = "Borrowed" if book.borrowed else "Available"
            print(f"{i}. {book.title} by {book.author} ({book.year}) - {status}")

    def borrow_book(self):
        self.view_books()
        if not self.books:
            return

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
            print(f"📖 Borrowed '{book.title}' by {book.author}.")

        except ValueError:
            print("❌ Invalid input!")

    def return_book(self):
        borrowed_books = [book for book in self.books if book.borrowed]
        if not borrowed_books:
            print("📭 No borrowed books.")
            return

        print("\n=== Borrowed Books ===")
        for i, book in enumerate(borrowed_books, 1):
            print(f"{i}. {book.title} by {book.author}")

        try:
            index = int(input("Enter book number to return: ")) - 1

            if index < 0 or index >= len(borrowed_books):
                print("❌ Invalid book number!")
                return

            book_to_return = borrowed_books[index]
            book_to_return.borrowed = False
            print(f"🔄 Returned '{book_to_return.title}'.")

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

def main():
    library = LibrarySystem()
    library.library_menu()

if __name__ == "__main__":
    main()