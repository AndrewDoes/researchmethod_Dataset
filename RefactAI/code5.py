import random

class Character:
    def __init__(self, name: str, max_hp: int, attack_min: int, attack_max: int, potions: int, heal_amount: int):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.potions = potions
        self.heal_amount = heal_amount

    def is_alive(self) -> bool:
        return self.hp > 0

    def attack(self, other: 'Character') -> int:
        damage = random.randint(self.attack_min, self.attack_max)
        other.hp = max(0, other.hp - damage)
        return damage

    def use_potion(self) -> int:
        if self.potions > 0 and self.hp < self.max_hp:
            heal = min(self.heal_amount, self.max_hp - self.hp)
            self.hp += heal
            self.potions -= 1
            return heal
        return 0

    def __str__(self):
        return f"{self.name} HP: {self.hp}/{self.max_hp} | Potions: {self.potions}"

def start_game() -> str:
    print("Welcome to the Ultimate Battle Game!")
    player_name = input("Enter your name: ")
    print(f"Hello {player_name}, get ready to fight!")
    return player_name

def player_turn(player: Character, enemy: Character):
    while True:
        print("\n1. Attack\n2. Use Potion\n3. Run")
        choice = input("Enter choice: ")
        if choice == "1":
            damage = player.attack(enemy)
            print(f"You attack the enemy for {damage} damage! Enemy HP: {enemy.hp}/{enemy.max_hp}")
            break
        elif choice == "2":
            heal = player.use_potion()
            if heal > 0:
                print(f"You used a potion! Restored {heal} HP. Your HP: {player.hp}/{player.max_hp}. Potions left: {player.potions}")
            else:
                print("You have no potions left or HP is full!")
            break
        elif choice == "3":
            print("You ran away! Game over.")
            return False
        else:
            print("Invalid choice.")
    return True

def enemy_turn(player: Character, enemy: Character):
    if enemy.hp < 30 and enemy.potions > 0:
        heal = enemy.use_potion()
        print(f"Enemy used a potion! Enemy HP: {enemy.hp}/{enemy.max_hp}. Enemy potions left: {enemy.potions}")
    else:
        damage = enemy.attack(player)
        print(f"Enemy attacks you for {damage} damage! Your HP: {player.hp}/{player.max_hp}")

def battle(player: Character, enemy: Character):
    while player.is_alive() and enemy.is_alive():
        if not player_turn(player, enemy):
            return
        if enemy.is_alive():
            enemy_turn(player, enemy)
        if not player.is_alive():
            print("You died! Game over.")
            return
        elif not enemy.is_alive():
            print("You defeated the enemy! You win!")
            return

def main():
    player_name = start_game()
    player = Character(player_name, max_hp=100, attack_min=10, attack_max=20, potions=3, heal_amount=20)
    enemy = Character("Enemy", max_hp=100, attack_min=5, attack_max=15, potions=1, heal_amount=15)
    battle(player, enemy)

if __name__ == "__main__":
    main()