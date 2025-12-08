#-------HIGHER OR LOWER GAME-------#

import game_data
import random

logo = """ __    __   __    _______  __    __   _______ .______        
|  |  |  | |  |  /  _____||  |  |  | |   ____||   _  \       
|  |__|  | |  | |  |  __  |  |__|  | |  |__   |  |_)  |      
|   __   | |  | |  | |_ | |   __   | |   __|  |      /       
|  |  |  | |  | |  |__| | |  |  |  | |  |____ |  |\  \----.  
|__|  |__| |__|  \______| |__|  |__| |_______|| _| `._____|                                                             
 __        ______   ____    __    ____  _______ .______      
|  |      /  __  \  \   \  /  \  /   / |   ____||   _  \     
|  |     |  |  |  |  \   \/    \/   /  |  |__   |  |_)  |    
|  |     |  |  |  |   \            /   |   __|  |      /     
|  `----.|  `--'  |    \    /\    /    |  |____ |  |\  \----.
|_______| \______/      \__/  \__/     |_______|| _| `._____|
"""

vs = """
____    ____   _______.
\   \  /   /  /       |
 \   \/   /  |   (----`
  \      /    \   \    
   \    / .----)   |   
    \__/  |_______/
"""

print(logo)
data_list = game_data.data
score = 0
game_continue = True
choice_b = random.choice(data_list)

def format_data(choice):
    """Takes the account data and returns the printable format"""
    account_name = choice["name"]
    account_description = choice["description"]
    account_country = choice["country"]
    return f"{account_name}, a {account_description} from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Takes the user's guess and follower counts and returns if the user got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

while game_continue:
    choice_a = choice_b
    choice_b = random.choice(data_list)
    if choice_a == choice_b:
        choice_b = random.choice(data_list)

    print(f"Compare A: {format_data(choice_a)}")
    print(vs)
    print(f"Against B: {format_data(choice_b)}")

    guess = input("Who has more followers? Type 'A' or 'B'").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = choice_a["follower_count"]
    b_follower_count = choice_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    print(f"{choice_a["name"]} has {a_follower_count} million followers. {choice_b["name"]} has {b_follower_count} million followers.")

    if is_correct:
        score = score + 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, you're wrong. Final score: {score}")
        game_continue = False

