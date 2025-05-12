import random

class NumberGuessingGame:
    def __init__(self):
        self.difficulty_settings = {
            "easy": (10, 20),
            "medium": (7, 50),
            "hard": (5, 100)
        }
        self.max_attempts = 10
        self.number_range = 20
        self.secret_number = None
        self.attempts = 0
        self.guessed_numbers = []

    def start_game(self):
        print("Welcome to the Messy Number Guessing Game!")
        self.set_difficulty()
        self.secret_number = random.randint(1, self.number_range)
        self.play_game()

    def set_difficulty(self):
        difficulty = input("Choose difficulty - Easy, Medium, Hard: ").strip().lower()
        if difficulty in self.difficulty_settings:
            self.max_attempts, self.number_range = self.difficulty_settings[difficulty]
        else:
            print("Invalid difficulty. Defaulting to Easy.")
            self.max_attempts, self.number_range = self.difficulty_settings["easy"]

    def play_game(self):
        while self.attempts < self.max_attempts:
            guess = self.get_guess()
            if guess is None:
                continue
            self.guessed_numbers.append(guess)
            self.attempts += 1

            if self.check_guess(guess):
                break

        if self.attempts == self.max_attempts:
            print(f"Game over! The correct number was {self.secret_number}.")
        self.ask_replay()

    def get_guess(self):
        try:
            guess = int(input(f"Guess a number between 1 and {self.number_range}: "))
            if guess < 1 or guess > self.number_range:
                print("Out of range! Try again.")
                return None
            if guess in self.guessed_numbers:
                print("You already guessed that number! Try another.")
                return None
            return guess
        except ValueError:
            print("Invalid input! Please enter a number.")
            return None

    def check_guess(self, guess):
        if guess < self.secret_number:
            print("Too low! Try again.")
        elif guess > self.secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
            return True
        return False

    def ask_replay(self):
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay == "yes":
            self.reset_game()
            self.start_game()
        else:
            print("Thanks for playing!")

    def reset_game(self):
        self.attempts = 0
        self.guessed_numbers = []

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()