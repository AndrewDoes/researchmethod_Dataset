# WindSurf Remastered/code4.py

# Constants
TAX_RATE = 0.08

# Data Structures
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.stock} left)"

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Global Variables
products = []
users = []

# Functions
def add_product():
    name = input("Enter product name: ")
    price = input("Enter price: ")
    stock = input("Enter stock quantity: ")
    products.append(Product(name, price, stock))

def display_products():
    print("\n--- Product List ---")
    for product in products:
        print(product)

def find_product(name):
    for product in products:
        if product.name == name:
            return product
    return None

def purchase_product():
    name = input("Enter product name: ")
    product = find_product(name)
    if product is None:
        print("Product not found!")
        return
    qty = int(input("Enter quantity: "))
    if product.stock < qty:
        print("Not enough stock!")
        return
    product.stock -= qty
    total = product.price * qty
    print(f"Total: ${total:.2f}")
    print(f"Total with tax: ${total + (total * TAX_RATE):.2f}")

def register_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    users.append(User(name, age, email))
    print("User registered!")

def main_menu():
    while True:
        print("\n1. Register\n2. Add Product\n3. View Products\n4. Purchase\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            add_product()
        elif choice == "3":
            display_products()
        elif choice == "4":
            purchase_product()
        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main_menu()