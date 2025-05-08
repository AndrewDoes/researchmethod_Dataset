# WindSurf/code15.py

class Product:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - {self.category} - ${self.price:.2f} - Stock: {self.stock}"

class Store:
    def __init__(self):
        self.products = []

    def add_product(self):
        """Add product to store"""
        name = input("Enter product name: ").strip()
        category = input("Enter product category: ").strip()
        price = float(input("Enter product price: ").strip())
        stock = int(input("Enter product stock: ").strip())
        self.products.append(Product(name, category, price, stock))
        print(f"Added '{name}' to store.")

    def view_products(self):
        """View products in store"""
        if not self.products:
            print("No products available.")
            return
        print("\n=== Store ===")
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product}")

    def calculate_tax(self, product):
        """Calculate tax for product"""
        tax_rates = {
            "Electronics": 0.18,
            "Clothing": 0.05,
            "Food": 0.12,
            "Other": 0.08
        }
        return product.price * tax_rates.get(product.category, tax_rates["Other"])

def store_menu():
    """Store menu"""
    store = Store()
    while True:
        print("\n1. Add Product\n2. View Products\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            store.add_product()
        elif choice == "2":
            store.view_products()
            if store.products:
                product_index = int(input("Enter product number to calculate tax: ")) - 1
                if 0 <= product_index < len(store.products):
                    product = store.products[product_index]
                    tax = store.calculate_tax(product)
                    print(f"Tax for '{product.name}': ${tax:.2f}")
                else:
                    print("Invalid product number!")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    store_menu()