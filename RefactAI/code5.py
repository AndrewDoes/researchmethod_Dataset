import random

class Character:
    def __init__(self, name, max_hp, attack_min, attack_max, potions, potion_heal):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.potions = potions
        self.potion_heal = potion_heal

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        damage = random.randint(self.attack_min, self.attack_max)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.name} attacks {target.name} for {damage} damage! {target.name} HP: {target.hp}/{target.max_hp}")

    def use_potion(self):
        if self.potions > 0 and self.hp < self.max_hp:
            heal = min(self.potion_heal, self.max_hp - self.hp)
            self.hp += heal
            self.potions -= 1
            print(f"{self.name} used a potion! Restored {heal} HP. {self.name} HP: {self.hp}/{self.max_hp}. Potions left: {self.potions}")
            return True
        elif self.potions == 0:
            print(f"{self.name} has no potions left!")
        else:
            print(f"{self.name} is already at full health!")
        return False

def start_game():
    print("Welcome to the Ultimate Battle Game!")
    player_name = input("Enter your name: ")
    print(f"Hello {player_name}, get ready to fight!")
    return player_name

def player_turn(player, enemy):
    print("\n1. Attack\n2. Use Potion\n3. Run")
    choice = input("Enter choice: ")
    if choice == "1":
        player.attack(enemy)
        return True
    elif choice == "2":
        player.use_potion()
        return True
    elif choice == "3":
        print("You ran away! Game over.")
        return False
    else:
        print("Invalid choice.")
        return True

def enemy_turn(enemy, player):
    if enemy.hp < 30 and enemy.potions > 0:
        enemy.use_potion()
    else:
        enemy.attack(player)

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        if not player_turn(player, enemy):
            return
        if enemy.is_alive():
            enemy_turn(enemy, player)
        if not player.is_alive():
            print("You died! Game over.")
            return
        elif not enemy.is_alive():
            print("You defeated the enemy! You win!")
            return

def main():
    player_name = start_game()
    player = Character(player_name, max_hp=100, attack_min=10, attack_max=20, potions=3, potion_heal=20)
    enemy = Character("Enemy", max_hp=100, attack_min=5, attack_max=15, potions=1, potion_heal=15)
    battle(player, enemy)

if __name__ == "__main__":
    main()