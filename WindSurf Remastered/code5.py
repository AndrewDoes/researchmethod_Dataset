# WindSurf Remastered/code5.py

import random

# Constants
PLAYER_MAX_HP = 100
ENEMY_MAX_HP = 100
PLAYER_ATTACK_MIN = 10
PLAYER_ATTACK_MAX = 20
ENEMY_ATTACK_MIN = 5
ENEMY_ATTACK_MAX = 15

# Data Structures
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = PLAYER_MAX_HP
        self.potions = 3

    def is_alive(self):
        return self.hp > 0

    def use_potion(self):
        if self.potions > 0:
            heal = 20
            if self.hp + heal > PLAYER_MAX_HP:
                heal = PLAYER_MAX_HP - self.hp
            self.hp += heal
            self.potions -= 1
            print(f"You used a potion! Restored {heal} HP. Your HP: {self.hp}/{PLAYER_MAX_HP}. Potions left: {self.potions}")
        else:
            print("You have no potions left!")

class Enemy:
    def __init__(self):
        self.hp = ENEMY_MAX_HP
        self.potions = 1

    def is_alive(self):
        return self.hp > 0

    def use_potion(self):
        if self.potions > 0:
            heal = 20
            if self.hp + heal > ENEMY_MAX_HP:
                heal = ENEMY_MAX_HP - self.hp
            self.hp += heal
            self.potions -= 1
            print(f"Enemy used a potion! Restored {heal} HP. Enemy HP: {self.hp}/{ENEMY_MAX_HP}. Potions left: {self.potions}")
        else:
            print("Enemy has no potions left!")

# Functions
def start_game():
    player_name = input("Enter your name: ")
    print(f"Hello {player_name}, get ready to fight!")
    return Player(player_name)

def attack(attacker, defender):
    damage = random.randint(PLAYER_ATTACK_MIN, PLAYER_ATTACK_MAX)
    defender.hp -= damage
    if defender.hp < 0:
        defender.hp = 0
    print(f"{attacker.name} attacks {defender.name} for {damage} damage! {defender.name} HP: {defender.hp}/{ENEMY_MAX_HP if isinstance(defender, Enemy) else PLAYER_MAX_HP}")

def enemy_attack(enemy, player):
    damage = random.randint(ENEMY_ATTACK_MIN, ENEMY_ATTACK_MAX)
    player.hp -= damage
    if player.hp < 0:
        player.hp = 0
    print(f"Enemy attacks {player.name} for {damage} damage! {player.name} HP: {player.hp}/{PLAYER_MAX_HP}")

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print("\n1. Attack\n2. Use Potion\n3. Run")
        choice = input("Enter choice: ")
        if choice == "1":
            attack(player, enemy)
            if enemy.is_alive():
                if enemy.hp < 30 and enemy.potions > 0:
                    enemy.use_potion()
                else:
                    enemy_attack(enemy, player)
        elif choice == "2":
            player.use_potion()
            enemy_attack(enemy, player)
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
    enemy = Enemy()
    battle(player, enemy)

if __name__ == "__main__":
    main()