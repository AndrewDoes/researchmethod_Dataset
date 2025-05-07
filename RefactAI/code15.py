class Product:
    TAX_MAP = {
        "Electronics": 18,
        "Clothing": 5,
        "Food": 12
    }
    DEFAULT_TAX = 8

    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.calculate_tax(category)

    @classmethod
    def calculate_tax(cls, category):
        return cls.TAX_MAP.get(category, cls.DEFAULT_TAX)

    def update(self, category, price, stock):
        self.category = category
        self.price = price
        self.stock = stock
        self.tax = self.calculate_tax(category)

    def __str__(self):
        return (f"Name: {self.name}, Category: {self.category}, Price: {self.price}, "
                f"Stock: {self.stock}, Tax: {self.tax}%")

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, category, price, stock):
        self.products.append(Product(name, category, price, stock))
        print("Product Added!")

    def display_products(self):
        print("\n--- Product List ---")
        if not self.products:
            print("No products found.")
        for p in self.products:
            print(p)

    def find_product(self, name):
        for p in self.products:
            if p.name == name:
                return p
        return None

    def update_product(self, name):
        p = self.find_product(name)
        if p:
            category = input("Enter new category: ")
            price = input("Enter new price: ")
            stock = input("Enter new stock quantity: ")
            p.update(category, price, stock)
            print("Product Updated!")
        else:
            print("Product not found!")

    def delete_product(self, name):
        before_count = len(self.products)
        self.products = [p for p in self.products if p.name != name]
        if len(self.products) < before_count:
            print("Product Deleted!")
        else:
            print("Product not found!")

def get_input(prompt, validate_fn=lambda x: True, error_msg="Invalid input!"):
    while True:
        value = input(prompt)
        if validate_fn(value):
            return value
        print(error_msg)

def main():
    manager = ProductManager()
    menu_options = {
        "1": "Add Product",
        "2": "Display Products",
        "3": "Update Product",
        "4": "Delete Product",
        "5": "Exit"
    }
    while True:
        print("\n" + "\n".join([f"{k}. {v}" for k, v in menu_options.items()]))
        choice = input("Enter choice: ")
        if choice == "1":
            print("Add Product")
            name = get_input("Enter product name: ", lambda x: bool(x.strip()), "Name cannot be empty!")
            category = get_input("Enter category: ", lambda x: bool(x.strip()), "Category cannot be empty!")
            price = get_input("Enter price: ", lambda x: x.replace('.', '', 1).isdigit(), "Price must be a number!")
            stock = get_input("Enter stock quantity: ", lambda x: x.isdigit(), "Stock must be a number!")
            manager.add_product(name, category, price, stock)
        elif choice == "2":
            manager.display_products()
        elif choice == "3":
            name = get_input("Enter product name to update: ", lambda x: bool(x.strip()), "Name cannot be empty!")
            manager.update_product(name)
        elif choice == "4":
            name = get_input("Enter product name to delete: ", lambda x: bool(x.strip()), "Name cannot be empty!")
            manager.delete_product(name)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()