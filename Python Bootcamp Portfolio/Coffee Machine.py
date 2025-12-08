#-------COFFEE MACHINE-------#

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
machine_on = True

def check_resources(order_ingredients):
    """Returns if resources are sufficient for an order."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        else:
            return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction(money_received, cost_of_drink):
    """Returns True if payment is accepted or False if payment is insufficient."""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry, that's not enough money. Payment refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")

while machine_on:
    choice = input("What would you like? Espresso, Latte, or Cappuccino:").lower()
    if choice == "off":
        machine_on = False
        print("Machine turning off. Goodbye.")
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


