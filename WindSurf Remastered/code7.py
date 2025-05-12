# WindSurf Remastered/code7.py

import random

# Constants
DIFFICULTY_LEVELS = {
    "easy": {"max_attempts": 10, "number_range": 20},
    "medium": {"max_attempts": 7, "number_range": 50},
    "hard": {"max_attempts": 5, "number_range": 100}
}

# Functions
def get_difficulty_level():
    while True:
        difficulty = input("Choose difficulty - Easy, Medium, Hard: ").strip().lower()
        if difficulty in DIFFICULTY_LEVELS:
            return DIFFICULTY_LEVELS[difficulty]
        print("Invalid difficulty. Please choose Easy, Medium, or Hard.")

def get_number_to_guess(number_range):
    return random.randint(1, number_range)

def get_user_guess(number_range):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {number_range}: "))
            if 1 <= guess <= number_range:
                return guess
            print("Out of range! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    print("Welcome to the Messy Number Guessing Game!")
    difficulty = get_difficulty_level()
    number_to_guess = get_number_to_guess(difficulty["number_range"])
    attempts = 0
    guessed_numbers = []

    while attempts < difficulty["max_attempts"]:
        guess = get_user_guess(difficulty["number_range"])
        if guess in guessed_numbers:
            print("You already guessed that number! Try another.")
            continue
        guessed_numbers.append(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

    if attempts == difficulty["max_attempts"]:
        print(f"Game over! The correct number was {number_to_guess}.")

def play_again():
    while True:
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay == "yes":
            return True
        elif replay == "no":
            print("Thanks for playing!")
            return False
        print("Invalid input! Please enter yes or no.")

def main():
    while True:
        play_game()
        if not play_again():
            break

if __name__ == "__main__":
    main()