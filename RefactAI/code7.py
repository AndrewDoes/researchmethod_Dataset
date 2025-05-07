import random

class NumberGuessingGame:
    def __init__(self):
        self.difficulty_settings = {
            "easy":    {"max_attempts": 10, "number_range": 20},
            "medium":  {"max_attempts": 7,  "number_range": 50},
            "hard":    {"max_attempts": 5,  "number_range": 100}
        }

    def get_difficulty(self):
        difficulty = input("Choose difficulty - Easy, Medium, Hard: ").strip().lower()
        settings = self.difficulty_settings.get(difficulty)
        if not settings:
            print("Invalid difficulty. Defaulting to Easy.")
            settings = self.difficulty_settings["easy"]
        return settings["max_attempts"], settings["number_range"]

    def get_guess(self, number_range, guessed_numbers):
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {number_range}: "))
                if guess < 1 or guess > number_range:
                    print("Out of range! Try again.")
                elif guess in guessed_numbers:
                    print("You already guessed that number! Try another.")
                else:
                    return guess
            except ValueError:
                print("Invalid input! Please enter a number.")

    def play_round(self):
        print("Welcome to the Clean Number Guessing Game!")
        max_attempts, number_range = self.get_difficulty()
        secret_number = random.randint(1, number_range)
        attempts = 0
        guessed_numbers = []

        while attempts < max_attempts:
            guess = self.get_guess(number_range, guessed_numbers)
            guessed_numbers.append(guess)
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                return

        print(f"Game over! The correct number was {secret_number}.")

    def start(self):
        while True:
            self.play_round()
            replay = input("Do you want to play again? (yes/no): ").strip().lower()
            if replay != "yes":
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    NumberGuessingGame().start()