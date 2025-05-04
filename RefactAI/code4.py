from dataclasses import dataclass, field
from typing import List, Optional

TAX_RATE = 0.08

@dataclass
class User:
    name: str
    age: int
    email: str

@dataclass
class Product:
    name: str
    price: float
    stock: int

@dataclass
class Store:
    users: List[User] = field(default_factory=list)
    products: List[Product] = field(default_factory=list)

    def register_user(self) -> None:
        name = input("Enter your name: ")
        age = self.get_int("Enter your age: ")
        email = input("Enter your email: ")
        self.users.append(User(name, age, email))
        print("User registered!")

    def add_product(self) -> None:
        name = input("Enter product name: ")
        price = self.get_float("Enter price: ")
        stock = self.get_int("Enter stock quantity: ")
        self.products.append(Product(name, price, stock))

    def display_products(self) -> None:
        print("\n--- Product List ---")
        for product in self.products:
            print(f"{product.name} - ${product.price:.2f} ({product.stock} left)")

    def find_product(self, name: str) -> Optional[Product]:
        for product in self.products:
            if product.name == name:
                return product
        return None

    def purchase(self) -> None:
        name = input("Enter product name: ")
        product = self.find_product(name)
        if not product:
            print("Product not found!")
            return
        qty = self.get_int("Enter quantity: ")
        if product.stock < qty:
            print("Not enough stock!")
            return
        product.stock -= qty
        total = product.price * qty
        print(f"Total: ${total:.2f}")
        print(f"Total with tax: ${total + (total * TAX_RATE):.2f}")

    @staticmethod
    def get_int(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

    @staticmethod
    def get_float(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def menu(self) -> None:
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

def main():
    store = Store()
    store.menu()

if __name__ == "__main__":
    main()