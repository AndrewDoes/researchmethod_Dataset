class User:
    def __init__(self, name: str, age: str, email: str):
        self.name = name
        self.age = age
        self.email = email

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

class Store:
    def __init__(self):
        self.users = []
        self.products = []
        self.tax = 0.08

    def register_user(self) -> None:
        """Register a new user"""
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        self.users.append(User(name, age, email))
        print("User registered!")

    def add_product(self) -> None:
        """Add a new product"""
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        self.products.append(Product(name, price, stock))

    def display_products(self) -> None:
        """Display all products"""
        print("\n--- Products ---")
        for product in self.products:
            print(f"{product.name} - ${product.price:.2f} - Stock: {product.stock}")

def main() -> None:
    store = Store()

    while True:
        print("\n--- Store Menu ---")
        print("1. Register user")
        print("2. Add product")
        print("3. Display products")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            store.register_user()
        elif choice == "2":
            store.add_product()
        elif choice == "3":
            store.display_products()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()