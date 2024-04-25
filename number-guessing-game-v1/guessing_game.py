"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# NOTES:
# Created additional functions for the app.
# I used time for the loading times between each user action.
# I made a startup menu for the user's convenience.
# User can either type upper or lower keys during the menu options.
# Added play again option once game is over.

import time
import random

lower_num = 1
higher_num = 100
max_attempts = 6

secret_num = random.randint(lower_num, higher_num)
game_title = "THE NUMBER GUESSING GAME"
game_title = game_title.upper()


def take_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_num} and {higher_num}: "))
            print()
            if lower_num <= guess <= higher_num:
                return guess

            else:
                print("Generating...")
                time.sleep(1)
                print("Invalid input. Try a number within the given range.")
                print()

        except Exception as e:
            time.sleep(.5)
            print("Invalid input. Try again.".format(e))
            print()


def check_guess(guess, secret_num):
    if guess == secret_num:
        print("Generating...")
        time.sleep(1)
        print()
        return "The number is correct!"

    elif guess < secret_num:
        print("Generating...")
        print()
        time.sleep(1)
        return "This number is too low! "

    else:
        print("Generating...")
        print()
        time.sleep(1)
        return "This number is too high! "


def start_game():
    attempts = 0
    won = False
    secret_num = random.randint(lower_num, higher_num)

    while attempts < max_attempts:
        attempts += 1
        guess = take_guess()
        result = check_guess(guess, secret_num)

        if result == "The number is correct!":
            print(f"Bingo! You got the secret number {secret_num} within {attempts} attempts.\n"
                  "Congratulations, you won the game!\n--GAMEOVER--")
            print()
            won = True
            break

        else:
            print(f"{result}Try again.")
            print("You have", max_attempts - attempts, "attempts left.")
            print()

    if not won:
        print(f"Bummer! You ran out of attempts. The secret number was {secret_num}")
        print("Thank you for playing. ""Try again another time.\n--GAME OVER--")
        print()

    while True:
        play_again = input("Do you want to play again? (Enter Y/N): ")
        if play_again == "y" or play_again == "Y":
            print("Loading game...")
            print()
            time.sleep(3)
            start_game()

        if play_again == "n" or play_again == "N":
            time.sleep(1)
            print("You just left the game.")
            print()
            exit()

        else:
            time.sleep(.3)
            print("Invalid input.")
            print()
            continue


print("""
....................................................................
....................................................................""")
print()
print("                  '''", game_title, "'''                       ")
print("""
....................................................................
....................................................................""")
print()
print()


def get_menu_options():
    menu_options = ('s', 'S', 'e', 'E', 'h', 'H')

    while True:
        user_input = input("Type 'S' to Start the game / 'E' to Exit / 'H' for Help: ")

        if user_input in menu_options:
            return user_input

        else:
            print("Invalid input. Try again!")
            print()


while True:
    user_input = get_menu_options()
    if user_input == 's' or user_input == 'S':
        print("Loading game...")
        time.sleep(3)
        print()
        print("Welcome to the Number Guessing Game!")
        print()
        break

    elif user_input == 'e' or user_input == 'E':
        print()
        time.sleep(.3)
        user_input = input("Do you wish to exit the game? (Enter Y/N): ")

        if user_input == 'y' or user_input == 'Y':
            time.sleep(.3)
            print("You left the game. ")
            print()
            exit()

        elif user_input == 'n' or user_input == 'N':
            time.sleep(.3)
            print()
            continue

        else:
            time.sleep(.3)
            print("Invalid input...")
            print()
            continue

    elif user_input == 'h' or user_input == 'H':
        print()
        time.sleep(1)
        print("**HOW TO PLAY**\n")
        print(
            "1) Type a random number of your preference and press Enter.\n"
            "2) If your selected number is the secret number, you win the game.\n"
            "3) You get 6 attempts in order to find the correct number.\n"
            "4) If your selected number is incorrect, you lose and the game is over.\n"
            )
        print()

if __name__ == "__main__":
    start_game()
