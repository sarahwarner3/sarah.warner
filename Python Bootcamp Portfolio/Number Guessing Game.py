#-------NUMBER GUESSING GAME-------#

import random
logo = """
  ▄████  █    ██ ▓█████   ██████   ██████    ▄▄▄█████▓ ██░ ██ ▓█████     ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
 ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀     ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄      ▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒   ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░       ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░       ░       ░  ░░ ░   ░         ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░ 
      ░    ░        ░  ░      ░        ░               ░  ░  ░   ░  ░            ░    ░            ░    ░         ░  ░   ░     
                                                                                                             ░                 
"""

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
# print(number)
playing_game = True
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.").lower()

if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
else:
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5

while playing_game is True:
    make_a_guess = int(input("Make a guess: "))
    if make_a_guess == number:
        playing_game = False
        print(f"You got it! The answer was {number}.")
    elif make_a_guess < number:
        print("Too low.")
        attempts = attempts - 1
        if attempts == 0:
            playing_game = False
            print(f"You lose! The number to guess was {number}.")
        else:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
    elif make_a_guess > number:
        print("Too high.")
        attempts = attempts - 1
        if attempts == 0:
            playing_game = False
            print(f"You lose! The number to guess was {number}.")
        else:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")


