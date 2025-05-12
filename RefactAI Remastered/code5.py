import random

class Player:
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
        target.hp = max(0, target.hp - damage)
        print(f"{self.name} attacks {target.name} for {damage} damage! {target.name} HP: {target.hp}/{target.max_hp}")

    def use_potion(self):
        if self.potions > 0:
            heal = min(self.potion_heal, self.max_hp - self.hp)
            self.hp += heal
            self.potions -= 1
            print(f"{self.name} used a potion! Restored {heal} HP. {self.name} HP: {self.hp}/{self.max_hp}. Potions left: {self.potions}")
        else:
            print(f"{self.name} has no potions left!")

class BattleGame:
    def __init__(self):
        self.player = None
        self.enemy = Player("Enemy", 100, 5, 15, 1, 15)

    def start_game(self):
        print("Welcome to the Ultimate Battle Game!")
        name = input("Enter your name: ")
        self.player = Player(name, 100, 10, 20, 3, 20)
        print(f"Hello {self.player.name}, get ready to fight!")

    def enemy_turn(self):
        if self.enemy.hp < 30 and self.enemy.potions > 0:
            self.enemy.use_potion()
        else:
            self.enemy.attack(self.player)

    def player_turn(self):
        print("\n1. Attack\n2. Use Potion\n3. Run")
        choice = input("Enter choice: ")
        if choice == "1":
            self.player.attack(self.enemy)
            if self.enemy.is_alive():
                self.enemy_turn()
        elif choice == "2":
            self.player.use_potion()
            if self.enemy.is_alive():
                self.enemy.attack(self.player)
        elif choice == "3":
            print("You ran away! Game over.")
            return False
        else:
            print("Invalid choice.")
        return True

    def battle(self):
        while self.player.is_alive() and self.enemy.is_alive():
            if not self.player_turn():
                return
            if not self.player.is_alive():
                print("You died! Game over.")
                return
            elif not self.enemy.is_alive():
                print("You defeated the enemy! You win!")
                return

def main():
    game = BattleGame()
    game.start_game()
    game.battle()

if __name__ == "__main__":
    main()