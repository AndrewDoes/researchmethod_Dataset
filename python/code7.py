import random

def start_game():
    print("Welcome to the Messy Number Guessing Game!")
    difficulty = input("Choose difficulty - Easy, Medium, Hard: ").strip().lower()
    if difficulty == "easy":
        max_attempts = 10
        number_range = 20
    elif difficulty == "medium":
        max_attempts = 7
        number_range = 50
    elif difficulty == "hard":
        max_attempts = 5
        number_range = 100
    else:
        print("Invalid difficulty. Defaulting to Easy.")
        max_attempts = 10
        number_range = 20

    secret_number = random.randint(1, number_range)
    attempts = 0
    guessed_numbers = []

    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between 1 and {number_range}: "))
            if guess < 1 or guess > number_range:
                print("Out of range! Try again.")
                continue
            if guess in guessed_numbers:
                print("You already guessed that number! Try another.")
                continue

            guessed_numbers.append(guess)
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    if attempts == max_attempts:
        print(f"Game over! The correct number was {secret_number}.")

    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        start_game()
    else:
        print("Thanks for playing!")

start_game()
