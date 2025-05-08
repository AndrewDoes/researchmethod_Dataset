import random

class NumberGuessingGame:
    def __init__(self):
        self.max_attempts = 10
        self.number_range = 20
        self.secret_number = 0
        self.attempts = 0
        self.guessed_numbers = []

    def start_game(self) -> None:
        """Start the number guessing game"""
        print("Welcome to the Refactored Number Guessing Game!")
        self.set_difficulty()
        self.secret_number = random.randint(1, self.number_range)
        self.play_game()

    def set_difficulty(self) -> None:
        """Set the difficulty level of the game"""
        difficulty_settings = {
            "easy": (10, 20),
            "medium": (7, 50),
            "hard": (5, 100)
        }
        difficulty = input("Choose difficulty - Easy, Medium, Hard: ").strip().lower()
        self.max_attempts, self.number_range = difficulty_settings.get(difficulty, (10, 20))
        if difficulty not in difficulty_settings:
            print("Invalid difficulty. Defaulting to Easy.")

    def play_game(self) -> None:
        """Play the number guessing game"""
        while self.attempts < self.max_attempts:
            guess = self.get_guess()
            if guess is None:
                continue
            self.guessed_numbers.append(guess)
            self.attempts += 1
            if self.check_guess(guess):
                break
        self.end_game()

    def get_guess(self) -> int:
        """Get the user's guess"""
        try:
            guess = int(input(f"Guess a number between 1 and {self.number_range}: "))
            if guess < 1 or guess > self.number_range:
                print("Invalid guess. Please try again.")
                return None
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def check_guess(self, guess: int) -> bool:
        """Check if the user's guess is correct"""
        if guess < self.secret_number:
            print("Too low!")
            return False
        elif guess > self.secret_number:
            print("Too high!")
            return False
        else:
            print("Congratulations! You guessed the number.")
            return True

    def end_game(self) -> None:
        """End the game"""
        print(f"\nGame over. You used {self.attempts} attempts.")
        play_again = input("Would you like to play again? (yes/no): ")
        if play_again.lower() == "yes":
            self.start_game()
        else:
            print("Thanks for playing!")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()