"""
Name: Ashish Panda
Description: Input loop
"""

try:
    from functions import inputs
    from database import options, history
except ModuleNotFoundError:
    print("*IMPORT ERROR*")

while True:
    user_input = input("\n> ")
    if user_input in options:
        try:
            if user_input == "?":
                inputs().print_help()
            elif user_input == "+":
                inputs().add()
        except KeyError:
            print("*INVALID INPUT*")
    else:
        print("*INVALID INPUT*")
        break