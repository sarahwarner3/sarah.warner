#-------CALCULATOR-------#

import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    continue_working = True
    number_1 = float(input("What's the first number?: "))

    while continue_working:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        number_2 = float(input("What's the next number?: "))
        answer = (operations[operation_symbol](number_1, number_2))
        print(f"{number_1} {operation_symbol} {number_2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.").lower()

        if choice == 'y':
            number_1 = answer
        else:
            continue_working = False
            print("\n" * 20)
            print(art.logo)
            calculator()

calculator()
