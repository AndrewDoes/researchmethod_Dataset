from typing import List, Optional, Tuple

class User:
    def __init__(self, name: str, age: str, email: str):
        self.name = namel
        self.age = age
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.age}) - {self.email}"

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.stock} left)"

class Store:
    TAX_RATE = 0.08

    def __init__(self):
        self.users: List[User] = []
        self.products: List[Product] = []

    def register_user(self) -> None:
        """Register a new user."""
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        self.users.append(User(name, age, email))
        print("User registered!")

    def add_product(self) -> None:
        """Add a new product to the store."""
        name = input("Enter product name: ")
        try:
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            self.products.append(Product(name, price, stock))
        except ValueError:
            print("Invalid price or stock quantity.")

    def display_products(self) -> None:
        """Display all products in the store."""
        print("\n--- Product List ---")
        for product in self.products:
            print(product)

    def find_product(self, name: str) -> Optional[Product]:
        """Find a product by name."""
        for product in self.products:
            if product.name == name:
                return product
        return None

    def purchase(self) -> None:
        """Purchase a product."""
        name = input("Enter product name: ")
        product = self.find_product(name)
        if not product:
            print("Product not found!")
            return
        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity.")
            return
        if product.stock < qty:
            print("Not enough stock!")
            return
        product.stock -= qty
        total = product.price * qty
        total_with_tax = total * (1 + self.TAX_RATE)
        print(f"Total: ${total:.2f}")
        print(f"Total with tax: ${total_with_tax:.2f}")

    def menu(self) -> None:
        """Main menu loop."""
        while True:
            print("\n1. Register\n2. Add Product\n3. View Products\n4. Purchase\n5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.add_product()
            elif choice == "3":
                self.display_products()
            elif choice == "4":
                self.purchase()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    store = Store()
    store.menu()