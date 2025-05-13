# Constants
CATEGORY_TAX_RATES = {
    "Electronics": 18,
    "Clothing": 5,
    "Food": 12,
    "Default": 8
}

# Data Structures
class Product:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.calculate_tax()

    def calculate_tax(self):
        return CATEGORY_TAX_RATES.get(self.category, CATEGORY_TAX_RATES["Default"])

    def update(self, category=None, price=None, stock=None):
        if category:
            self.category = category
            self.tax = self.calculate_tax()
        if price:
            self.price = price
        if stock:
            self.stock = stock

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock}, Tax: {self.tax}%"

# Functions
class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self):
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = input("Enter price: ")
        stock = input("Enter stock quantity: ")
        self.products.append(Product(name, category, price, stock))
        print("Product Added!")

    def display_products(self):
        print("\n--- Product List ---")
        for product in self.products:
            print(product)

    def update_product(self):
        prod_name = input("Enter product name to update: ")
        for product in self.products:
            if product.name == prod_name:
                product.update(
                    category=input("Enter new category: "),
                    price=input("Enter new price: "),
                    stock=input("Enter new stock quantity: ")
                )
                print("Product Updated!")
                return
        print("Product not found!")

    def delete_product(self):
        prod_name = input("Enter product name to delete: ")
        self.products = [p for p in self.products if p.name != prod_name]
        print("Product Deleted!")

# Main function
def main():
    product_manager = ProductManager()
    while True:
        print("\n1. Add Product\n2. Display Products\n3. Update Product\n4. Delete Product\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            product_manager.add_product()
        elif choice == "2":
            product_manager.display_products()
        elif choice == "3":
            product_manager.update_product()
        elif choice == "4":
            product_manager.delete_product()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()