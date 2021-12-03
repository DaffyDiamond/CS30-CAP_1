"""
Name: Ashish Panda
Description: Input loop
"""

try:
    from functions import inputs, clear
    from database import options, history
except ModuleNotFoundError:
    print("*IMPORT ERROR*")


def input_loop():
    while True:
        user_input = input("\n> ")
        if user_input in options:
            if user_input.lower() == "q":
                clear()
                break
            elif user_input == "?":
                clear()
                inputs().print_help()
            elif user_input == "+":
                clear()
                inputs().add()
        else:
            print("*INVALID INPUT*")
