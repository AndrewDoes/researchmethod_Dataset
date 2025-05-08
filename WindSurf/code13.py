# WindSurf/code13.py

class Book:
    def __init__(self, title, author, publication_year, borrowed=False):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = borrowed

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.publication_year}. Borrowed: {self.borrowed}"

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self):
        """Add book to library"""
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        publication_year = int(input("Enter book publication year: ").strip())
        self.books.append(Book(title, author, publication_year))
        print(f"Added '{title}' to library.")

    def view_books(self):
        """View books in library"""
        if not self.books:
            print("No books available.")
            return
        print("\n=== Library ===")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def borrow_book(self):
        """Borrow book from library"""
        self.view_books()
        try:
            index = int(input("Enter book number: ")) - 1
            if index < 0 or index >= len(self.books):
                print("Invalid book number!")
                return
            book = self.books[index]
            if book.borrowed:
                print("Book is already borrowed!")
                return
            book.borrowed = True
            self.borrowed_books.append(book)
            print(f"Borrowed '{book.title}'")
        except ValueError:
            print("Invalid input!")

    def return_book(self):
        """Return book to library"""
        if not self.borrowed_books:
            print("No borrowed books.")
            return
        print("\n=== Borrowed Books ===")
        for i, book in enumerate(self.borrowed_books, start=1):
            print(f"{i}. {book}")
        try:
            index = int(input("Enter book number to return: ")) - 1
            if index < 0 or index >= len(self.borrowed_books):
                print("Invalid book number!")
                return
            returned_book = self.borrowed_books.pop(index)
            for book in self.books:
                if book.title == returned_book.title:
                    book.borrowed = False
                    break
            print(f"Returned '{returned_book.title}'")
        except ValueError:
            print("Invalid input!")

def library_menu():
    """Library menu"""
    library = Library()
    while True:
        print("\n1. Add Book\n2. View Books\n3. Borrow Book\n4. Return Book\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    library_menu()