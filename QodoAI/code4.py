from typing import List, Tuple

class User:
    def __init__(self, name: str, age: str, email: str) -> None:
        self.name = name
        self.age = age
        self.email = email

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"


class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f} ({self.stock} left)"

    def update_stock(self, quantity: int) -> None:
        if self.stock < quantity:
            raise ValueError("Not enough stock!")
        self.stock -= quantity


class Store:
    def __init__(self, tax_rate: float = 0.08) -> None:
        self.users: List[User] = []
        self.products: List[Product] = []
        self.tax_rate = tax_rate

    def register_user(self) -> None:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        self.users.append(User(name, age, email))
        print("User registered!")

    def add_product(self) -> None:
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        self.products.append(Product(name, price, stock))

    def display_products(self) -> None:
        print("\n--- Product List ---")
        for product in self.products:
            print(product)

    def find_product(self, name: str) -> Product:
        for product in self.products:
            if product.name == name:
                return product
        raise ValueError("Product not found!")

    def purchase_product(self) -> None:
        try:
            name = input("Enter product name: ")
            product = self.find_product(name)
            qty = int(input("Enter quantity: "))
            product.update_stock(qty)
            total = product.price * qty
            print(f"Total: ${total:.2f}")
            print(f"Total with tax: ${total + (total * self.tax_rate):.2f}")
        except ValueError as e:
            print(e)

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
                self.purchase_product()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")


def main() -> None:
    store = Store()
    store.menu()


if __name__ == "__main__":
    main()
