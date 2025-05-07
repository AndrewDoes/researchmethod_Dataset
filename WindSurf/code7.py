# WindSurf/code7.py

import random

class Game:
    def __init__(self):
        self.difficulty_levels = {
            "easy": {"max_attempts": 10, "number_range": 20},
            "medium": {"max_attempts": 7, "number_range": 50},
            "hard": {"max_attempts": 5, "number_range": 100}
        }

    def get_difficulty_level(self):
        while True:
            difficulty = input("Choose difficulty - Easy, Medium, Hard: ").strip().lower()
            if difficulty in self.difficulty_levels:
                return self.difficulty_levels[difficulty]
            print("Invalid difficulty level. Please choose Easy, Medium, or Hard.")

    def play(self):
        print("Welcome to the Messy Number Guessing Game!")
        difficulty_level = self.get_difficulty_level()
        number_to_guess = random.randint(1, difficulty_level["number_range"])
        attempts = 0
        while attempts < difficulty_level["max_attempts"]:
            try:
                guess = int(input(f"Guess a number between 1 and {difficulty_level['number_range']}: "))
                attempts += 1
                if guess == number_to_guess:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    return
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"Sorry, you didn't guess the number. The number was {number_to_guess}.")

def start_game():
    game = Game()
    game.play()

if __name__ == "__main__":
    start_game()