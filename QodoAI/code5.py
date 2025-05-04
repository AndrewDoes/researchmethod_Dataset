import random

class Character:
    def __init__(self, name: str, max_hp: int, attack_range: Tuple[int, int], potions: int) -> None:
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack_min, self.attack_max = attack_range
        self.potions = potions

    def attack(self, target: 'Character') -> None:
        damage = random.randint(self.attack_min, self.attack_max)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.name} attacks {target.name} for {damage} damage! {target.name} HP: {target.hp}/{target.max_hp}")

    def use_potion(self) -> None:
        if self.potions > 0:
            heal = min(20, self.max_hp - self.hp)
            self.hp += heal
            self.potions -= 1
            print(f"{self.name} used a potion! Restored {heal} HP. {self.name} HP: {self.hp}/{self.max_hp}. Potions left: {self.potions}")
        else:
            print(f"{self.name} has no potions left!")

    def is_alive(self) -> bool:
        return self.hp > 0


class Game:
    def __init__(self) -> None:
        self.player = Character(name="", max_hp=100, attack_range=(10, 20), potions=3)
        self.enemy = Character(name="Enemy", max_hp=100, attack_range=(5, 15), potions=1)

    def start_game(self) -> None:
        print("Welcome to the Ultimate Battle Game!")
        self.player.name = input("Enter your name: ")
        print(f"Hello {self.player.name}, get ready to fight!")

    def battle(self) -> None:
        while self.player.is_alive() and self.enemy.is_alive():
            print("\n1. Attack\n2. Use Potion\n3. Run")
            choice = input("Enter choice: ")
            if choice == "1":
                self.player.attack(self.enemy)
                self.enemy_turn()
            elif choice == "2":
                self.player.use_potion()
                self.enemy.attack(self.player)
            elif choice == "3":
                print("You ran away! Game over.")
                return
            else:
                print("Invalid choice.")

            self.check_game_over()

    def enemy_turn(self) -> None:
        if self.enemy.hp < 30 and self.enemy.potions > 0:
            self.enemy.use_potion()
        else:
            self.enemy.attack(self.player)

    def check_game_over(self) -> None:
        if not self.player.is_alive():
            print("You died! Game over.")
        elif not self.enemy.is_alive():
            print("You defeated the enemy! You win!")


def main() -> None:
    game = Game()
    game.start_game()
    game.battle()


if __name__ == "__main__":
    main()
