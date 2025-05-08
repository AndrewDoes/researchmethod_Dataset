import random

class Game:
    def __init__(self):
        self.player_name = ""
        self.player_hp = 100
        self.player_max_hp = 100
        self.enemy_hp = 100
        self.enemy_max_hp = 100
        self.potions = 3
        self.enemy_potions = 1
        self.player_attack_min = 10
        self.player_attack_max = 20
        self.enemy_attack_min = 5
        self.enemy_attack_max = 15
        self.turn = 0

    def start_game(self) -> None:
        """Start the game"""
        self.player_name = input("Enter your name: ")
        print(f"Welcome, {self.player_name}!")

    def battle(self) -> None:
        """Start the battle"""
        while self.player_hp > 0 and self.enemy_hp > 0:
            self.turn += 1
            print(f"\n--- Turn {self.turn} ---")
            print(f"{self.player_name}'s HP: {self.player_hp}/{self.player_max_hp}")
            print(f"Enemy's HP: {self.enemy_hp}/{self.enemy_max_hp}")

            action = input("Enter your action (1) Attack, (2) Heal, (3) Run: ")
            if action == "1":
                self.player_attack()
            elif action == "2":
                self.player_heal()
            elif action == "3":
                self.player_run()
            else:
                print("Invalid action. Please try again.")

            if self.enemy_hp > 0:
                self.enemy_attack()

        if self.player_hp > 0:
            print(f"\n{self.player_name} wins!")
        else:
            print(f"\n{self.player_name} loses!")

    def player_attack(self) -> None:
        """Player attacks the enemy"""
        attack = random.randint(self.player_attack_min, self.player_attack_max)
        self.enemy_hp -= attack
        print(f"{self.player_name} attacks the enemy for {attack} damage!")

    def player_heal(self) -> None:
        """Player heals themselves"""
        if self.potions > 0:
            heal = random.randint(10, 20)
            self.player_hp += heal
            self.potions -= 1
            print(f"{self.player_name} heals themselves for {heal} HP!")
        else:
            print(f"{self.player_name} has no potions left!")

    def player_run(self) -> None:
        """Player runs away from the battle"""
        print(f"{self.player_name} runs away from the battle!")
        self.player_hp = 0

    def enemy_attack(self) -> None:
        """Enemy attacks the player"""
        attack = random.randint(self.enemy_attack_min, self.enemy_attack_max)
        self.player_hp -= attack
        print(f"Enemy attacks {self.player_name} for {attack} damage!")

def main() -> None:
    game = Game()
    game.start_game()
    game.battle()

if __name__ == "__main__":
    main()