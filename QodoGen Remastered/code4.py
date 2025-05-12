
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.stock} left)"


class ECommerceSystem:
    def __init__(self, tax_rate=0.08):
        self.users = []
        self.products = []
        self.tax_rate = tax_rate

    def register_user(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        self.users.append(User(name, age, email))
        print("User registered!")

    def add_product(self):
        name = input("Enter product name: ")
        price = input("Enter price: ")
        stock = input("Enter stock quantity: ")
        self.products.append(Product(name, price, stock))

    def display_products(self):
        print("\n--- Product List ---")
        for product in self.products:
            print(product)

    def find_product(self, name):
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
        if not product.update_stock(qty):
            print("Not enough stock!")
            return
        total = product.price * qty
        print(f"Total: ${total:.2f}")
        print(f"Total with tax: ${total + (total * self.tax_rate):.2f}")

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


def main():
    system = ECommerceSystem()
    system.menu()


if __name__ == "__main__":
    main()
