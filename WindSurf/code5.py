import random

class Player:
    def __init__(self, name, max_hp):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.potions = 3

    def is_alive(self):
        return self.hp > 0

    def use_potion(self):
        if self.potions > 0:
            heal = 20
            if self.hp + heal > self.max_hp:
                heal = self.max_hp - self.hp
            self.hp += heal
            self.potions -= 1
            print(f"You used a potion! Restored {heal} HP. Your HP: {self.hp}/{self.max_hp}. Potions left: {self.potions}")
        else:
            print("You have no potions left!")

    def attack(self, enemy):
        damage = random.randint(10, 20)
        enemy.hp -= damage
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"You attack the enemy for {damage} damage! Enemy HP: {enemy.hp}/{enemy.max_hp}")


class Enemy:
    def __init__(self, max_hp):
        self.hp = max_hp
        self.max_hp = max_hp
        self.potions = 1

    def is_alive(self):
        return self.hp > 0

    def use_potion(self):
        if self.potions > 0 and self.hp < self.max_hp:
            heal = 15
            if self.hp + heal > self.max_hp:
                heal = self.max_hp - self.hp
            self.hp += heal
            self.potions -= 1
            print(f"Enemy used a potion! Enemy HP: {self.hp}/{self.max_hp}. Enemy potions left: {self.potions}")

    def attack(self, player):
        damage = random.randint(5, 15)
        player.hp -= damage
        if player.hp < 0:
            player.hp = 0
        print(f"Enemy attacks you for {damage} damage! Your HP: {player.hp}/{player.max_hp}")


def start_game():
    print("Welcome to the Ultimate Battle Game!")
    player_name = input("Enter your name: ")
    print(f"Hello {player_name}, get ready to fight!")
    return Player(player_name, 100)


def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print("\n1. Attack\n2. Use Potion\n3. Run")
        choice = input("Enter choice: ")
        if choice == "1":
            player.attack(enemy)
            if enemy.is_alive():
                if enemy.hp < 30 and enemy.potions > 0:
                    enemy.use_potion()
                else:
                    enemy.attack(player)
        elif choice == "2":
            player.use_potion()
            enemy.attack(player)
        elif choice == "3":
            print("You ran away! Game over.")
            return
        else:
            print("Invalid choice.")

        if not player.is_alive():
            print("You died! Game over.")
            return
        elif not enemy.is_alive():
            print("You defeated the enemy! You win!")
            return


def main():
    player = start_game()
    enemy = Enemy(100)
    battle(player, enemy)


if __name__ == "__main__":
    main()