class User:
    def __init__(self, name: str, age: str, email: str):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"


class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.stock} left)"


class Store:
    def __init__(self):
        self.users = []
        self.products = []
        self.tax_rate = 0.08

    def register_user(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        self.users.append(User(name, age, email))
        print("User registered!")

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        self.products.append(Product(name, price, stock))

    def display_products(self):
        print("\n--- Product List ---")
        for product in self.products:
            print(product)

    def find_product(self, name: str) -> Product:
        for product in self.products:
            if product.name == name:
                return product
        return None

    def purchase_product(self):
        name = input("Enter product name: ")
        product = self.find_product(name)
        if not product:
            print("Product not found!")
            return
        qty = int(input("Enter quantity: "))
        if product.stock < qty:
            print("Not enough stock!")
            return
        product.stock -= qty
        total = product.price * qty
        total_with_tax = total + (total * self.tax_rate)
        print(f"Total: ${total:.2f}")
        print(f"Total with tax: ${total_with_tax:.2f}")

    def menu(self):
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


if __name__ == "__main__":
    store = Store()
    store.menu()