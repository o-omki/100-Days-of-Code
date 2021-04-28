import random
from os import system, name

def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def number_guessing_game():
    print("    **Welcome to the Number Guessing Game!** \n\nI'm choosing a number between 1 to 100.")
    difficulty = input("Choose the difficulty level: Type 'easy' or 'hard': ").lower()
    max_attempts = None
    end_of_game = False

    if difficulty == "easy":
        max_attempts = 10
    elif difficulty == "hard":
        max_attempts = 5
    else:
        print("Incorrect Input!")
        return

    num = random.randrange(1, 101)

    while not end_of_game:
        print(f"\nYou have {max_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == num:
            print(f"You got it! The correct number was {num}")
            end_of_game = True 
            
        elif guess < num:
            print("Too low.")
            max_attempts -= 1

        else:
            print("Too high.")
            max_attempts -= 1
            
        if max_attempts == 0:
            print(f"You lose. You've run out of guesses. The number was {num}")  
            end_of_game = True

while input("\nPlay a number guessing game? (y / n): ") == 'y':
    clear_screen()
    number_guessing_game()