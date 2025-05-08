# WindSurf/code15.py

# Constants
TAX_RATES = {
    "Electronics": 18,
    "Clothing": 5,
    "Food": 12
}

class Product:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.calculate_tax()

    def calculate_tax(self):
        return TAX_RATES.get(self.category, 8)

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock}, Tax: {self.tax}%"

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self):
        product = self._get_product_details()
        self.products.append(product)
        print("Product Added!")

    def _get_product_details(self):
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = input("Enter price: ")
        stock = input("Enter stock quantity: ")
        return Product(name, category, price, stock)

    def display_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\n--- Product List ---")
        for product in self.products:
            print(product)

    def update_product(self):
        name = input("Enter product name to update: ")
        product = self._find_product(name)
        if product:
            product.price = input("Enter new price: ")
            product.stock = input("Enter new stock quantity: ")
            print("Product Updated!")
        else:
            print("Product not found!")

    def _find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def delete_product(self):
        name = input("Enter product name to delete: ")
        self.products = [product for product in self.products if product.name != name]
        print("Product Deleted!")

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
            print("Invalid choice!")

if __name__ == "__main__":
    main()