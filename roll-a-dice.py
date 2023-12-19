import random

def roll_dice():
    return random.randint(1, 6)

def print_dice(number):
    if number == 1:
        print("---------")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print("---------")
    elif number == 2:
        print("---------")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print("---------")
    elif number == 3:
        print("---------")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print("---------")
    elif number == 4:
        print("---------")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print("---------")
    elif number == 5:
        print("---------")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print("---------")
    elif number == 6:
        print("---------")
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
        print("---------")

response = input("Roll a dice? (y/n)")

while response == "y":
    result = roll_dice()
    print(result)
    response = input("Do you want to roll again? (y/n): ")

print("Thanks for playing! Goodbye.")