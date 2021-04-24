# Hangman game that runs in the command terminal.
import random
from os import system, name
from time import sleep
import data.hangman_figures as figures
from data.hangman_words import word_list


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

lives = 6
chosen_word = random.choice(word_list)
chosen_word = "apple"
word = []
game_end = False

for _ in range(len(chosen_word)):
    word += '_'

clear_screen()
print(figures.title)
print("BIG BRAIN TIME! Guess the upcoming word...")
sleep(2)

while not game_end:
    clear_screen()
    if '_' not in word:
        print(figures.hangman_stages[7])
        print(word)
        print("\nYAY! You win! The man was saved!")
        game_end = True
        break

    print(figures.hangman_stages[lives])
    print(word)

    if lives == 0:
        print("\nGame over! You couldn't save the man.")
        print(str(chosen_word).upper() + " was the correct word.")
        game_end = True
        break

    guess = input("\nGuess a letter: ").lower()
    if guess not in chosen_word:
        print(f"You've guessed '{guess}'', that's not present in the word. You lose a life :(")
        lives -=1
        sleep(2)
    
    if guess in word:
        print(f"You've already guessed '{guess}'")
        sleep(1)

    else:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                word[i] = letter


    

