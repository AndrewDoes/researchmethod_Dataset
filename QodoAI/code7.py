import random

class NumberGuessingGame:
    def __init__(self) -> None:
        self.difficulty_settings = {
            "easy": {"max_attempts": 10, "number_range": 20},
            "medium": {"max_attempts": 7, "number_range": 50},
            "hard": {"max_attempts": 5, "number_range": 100},
        }
        self.max_attempts = 10
        self.number_range = 20
        self.secret_number = 0
        self.attempts = 0
        self.guessed_numbers = []

    def start_game(self) -> None:
        print("Welcome to the Number Guessing Game!")
        self.set_difficulty()
        self.secret_number = random.randint(1, self.number_range)
        self.play_game()

    def set_difficulty(self) -> None:
        difficulty = input("Choose difficulty - Easy, Medium, Hard: ").strip().lower()
        settings = self.difficulty_settings.get(difficulty)
        if settings:
            self.max_attempts = settings["max_attempts"]
            self.number_range = settings["number_range"]
        else:
            print("Invalid difficulty. Defaulting to Easy.")

    def play_game(self) -> None:
        while self.attempts < self.max_attempts:
            guess = self.get_guess()
            if guess is None:
                continue
            self.process_guess(guess)
            if guess == self.secret_number:
                print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                break
        else:
            print(f"Game over! The correct number was {self.secret_number}.")
        self.ask_replay()

    def get_guess(self) -> int:
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

    def process_guess(self, guess: int) -> None:
        self.guessed_numbers.append(guess)
        self.attempts += 1
        if guess < self.secret_number:
            print("Too low! Try again.")
        elif guess > self.secret_number:
            print("Too high! Try again.")

    def ask_replay(self) -> None:
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay == "yes":
            self.reset_game()
            self.start_game()
        else:
            print("Thanks for playing!")

    def reset_game(self) -> None:
        self.attempts = 0
        self.guessed_numbers = []

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()
