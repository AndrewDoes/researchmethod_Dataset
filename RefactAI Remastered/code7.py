import random

class NumberGuessingGame:
    DIFFICULTY_SETTINGS = {
        "easy": {"max_attempts": 10, "number_range": 20},
        "medium": {"max_attempts": 7, "number_range": 50},
        "hard": {"max_attempts": 5, "number_range": 100}
    }

    def __init__(self):
        self.max_attempts = 10
        self.number_range = 20
        self.secret_number = None
        self.attempts = 0
        self.guessed_numbers = []

    def choose_difficulty(self):
        difficulty = input("Choose difficulty - Easy, Medium, Hard: ").strip().lower()
        settings = self.DIFFICULTY_SETTINGS.get(difficulty)
        if not settings:
            print("Invalid difficulty. Defaulting to Easy.")
            settings = self.DIFFICULTY_SETTINGS["easy"]
        self.max_attempts = settings["max_attempts"]
        self.number_range = settings["number_range"]

    def get_guess(self):
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.number_range}: "))
                if guess < 1 or guess > self.number_range:
                    print("Out of range! Try again.")
                elif guess in self.guessed_numbers:
                    print("You already guessed that number! Try another.")
                else:
                    return guess
            except ValueError:
                print("Invalid input! Please enter a number.")

    def play_round(self):
        self.secret_number = random.randint(1, self.number_range)
        self.attempts = 0
        self.guessed_numbers = []

        while self.attempts < self.max_attempts:
            guess = self.get_guess()
            self.guessed_numbers.append(guess)
            self.attempts += 1

            if guess < self.secret_number:
                print("Too low! Try again.")
            elif guess > self.secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                return

        print(f"Game over! The correct number was {self.secret_number}.")

    def play(self):
        print("Welcome to the Messy Number Guessing Game!")
        while True:
            self.choose_difficulty()
            self.play_round()
            replay = input("Do you want to play again? (yes/no): ").strip().lower()
            if replay != "yes":
                print("Thanks for playing!")
                break

def main():
    game = NumberGuessingGame()
    game.play()

if __name__ == "__main__":
    main()