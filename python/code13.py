books = []
borrowed_books = []

def add_book():
    print("\n=== Add Book ===")
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter year: ").strip()
    
    if not year.isdigit():
        print("❌ Invalid year!")
        return
    
    books.append([title, author, int(year), False])  # False means not borrowed
    print(f"✅ Added '{title}' by {author} ({year}).")

def view_books():
    if not books:
        print("📭 No books available.")
        return
    
    print("\n=== Library Books ===")
    for i, book in enumerate(books):
        status = "Borrowed" if book[3] else "Available"
        print(f"{i+1}. {book[0]} by {book[1]} ({book[2]}) - {status}")

def borrow_book():
    view_books()
    
    try:
        index = int(input("Enter book number to borrow: ")) - 1

        if index < 0 or index >= len(books):
            print("❌ Invalid book number!")
            return
        
        if books[index][3]:
            print("❌ This book is already borrowed!")
            return

        books[index][3] = True
        borrowed_books.append(books[index])
        print(f"📖 Borrowed '{books[index][0]}' by {books[index][1]}.")

    except ValueError:
        print("❌ Invalid input!")

def return_book():
    if not borrowed_books:
        print("📭 No borrowed books.")
        return

    print("\n=== Borrowed Books ===")
    for i, book in enumerate(borrowed_books):
        print(f"{i+1}. {book[0]} by {book[1]}")

    try:
        index = int(input("Enter book number to return: ")) - 1

        if index < 0 or index >= len(borrowed_books):
            print("❌ Invalid book number!")
            return

        returned_book = borrowed_books.pop(index)
        for book in books:
            if book == returned_book:
                book[3] = False
                break
        
        print(f"🔄 Returned '{returned_book[0]}'.")

    except ValueError:
        print("❌ Invalid input!")

def library_menu():
    while True:
        print("\n1. Add Book\n2. View Books\n3. Borrow Book\n4. Return Book\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    library_menu()
