# WindSurf/code18.py

import random

class Drink:
    def __init__(self, name, size, price, ice=True, sugar=True):
        self.name = name
        self.size = size
        self.price = price
        self.ice = ice
        self.sugar = sugar
        self.custom_note = ""

    def __str__(self):
        return f"Name: {self.name}, Size: {self.size}, Price: {self.price}, Ice: {self.ice}, Sugar: {self.sugar}"

    def add_custom_note(self, note):
        self.custom_note = note

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Price: {self.price}")
        print(f"Ice: {self.ice}")
        print(f"Sugar: {self.sugar}")
        if self.custom_note:
            print(f"Custom Note: {self.custom_note}")

class DrinkMenu:
    def __init__(self):
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    def display_menu(self):
        for i, drink in enumerate(self.drinks, start=1):
            print(f"{i}. {drink.name}")

    def get_drink(self, index):
        try:
            return self.drinks[index - 1]
        except IndexError:
            print("Invalid index")
            return None

def main():
    drink_menu = DrinkMenu()

    while True:
        print("\n1. Add Drink\n2. Display Menu\n3. Get Drink\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter drink name: ")
            size = input("Enter drink size: ")
            price = float(input("Enter drink price: "))
            ice = input("Enter ice preference (yes/no): ").lower() == "yes"
            sugar = input("Enter sugar preference (yes/no): ").lower() == "yes"
            drink = Drink(name, size, price, ice, sugar)
            drink_menu.add_drink(drink)
        elif choice == "2":
            drink_menu.display_menu()
        elif choice == "3":
            index = int(input("Enter drink index: "))
            drink = drink_menu.get_drink(index)
            if drink:
                drink.display_details()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()