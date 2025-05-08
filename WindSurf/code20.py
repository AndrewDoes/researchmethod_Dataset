# WindSurf/code20.py

import random

class MenuItem:
    def __init__(self, name: str, price: float, description: str = ""):
        self.name = name
        self.price = price
        self.description = description

    def get_info(self) -> str:
        return f"{self.name} - ${self.price:.2f}: {self.description}"

class Menu:
    def __init__(self):
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def remove_item(self, item: MenuItem) -> None:
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found")

    def display_menu(self) -> None:
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.get_info()}")

def main():
    menu = Menu()

    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Display Menu\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            description = input("Enter item description (optional): ")
            item = MenuItem(name, price, description)
            menu.add_item(item)
        elif choice == "2":
            name = input("Enter item name to remove: ")
            for item in menu.items:
                if item.name == name:
                    menu.remove_item(item)
                    break
            else:
                print("Item not found")
        elif choice == "3":
            menu.display_menu()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()