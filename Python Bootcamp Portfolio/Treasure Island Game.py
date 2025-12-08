#-------TREASURE ISLAND GAME-------#

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad_1 = (input("You are at a crossroad. Which way would you like to go: left or right"))

if crossroad_1 == "Left" or crossroad_1 == "left":
    crossroad_2 = (input("You have arrived at a lake and can see an island. Do you wait for a boat or swim?"))
    if crossroad_2 == "Wait" or crossroad_2 == "wait" or crossroad_2 == "wait for a boat":
        crossroad_3 = input("You make it to the island and come upon a house with 3 doors. Which door do you choose: "
                            "red, yellow, or blue?")
        if crossroad_3 == "Red" or crossroad_3 == "red" or crossroad_3 == "red door":
            print("The door locks behind you. You flip on the lights to see a killer clown waiting for you. RIP. Game Over.")
        elif crossroad_3 == "Blue" or crossroad_3 == "blue" or crossroad_3 == "blue door":
            print("The door locks behind you. You flip on what you think is a light switch. Suddenly the floor crumbles "
                  "away and below is flowing lava! You have been incinerated. RIP. Game Over.")
        elif crossroad_3 == "Yellow" or crossroad_3 == "yellow" or crossroad_3 == "yellow door":
            print("Congrats, you've found the treasure. You win!")
        else:
            print("You're answer is invalid. Game Over.")
    elif crossroad_2 == "Swim" or crossroad_2 == "swim" or crossroad_2 == "swim to the island":
        print("A school of piranhas has ripped to to shreds. RIP. Game Over.")
    else:
        print("You're answer is invalid. Game Over.")
elif crossroad_1 == "Right" or crossroad_1 == "right" or crossroad_1 == "go right":
    print("You fell into a deep dark well with no way out. Game Over.")
else:
    print("You're answer is invalid. Game Over.")

