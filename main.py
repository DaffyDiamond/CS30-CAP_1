"""
Name: Ashish Panda
Description: Input loop
"""

try:
    from functions import Inputs, clear
    from database import OPTIONS
except ModuleNotFoundError:
    print("*IMPORT ERROR*")


def input_loop():
    """Main loop that user can interact with"""
    while True:
        user_input = input("\n> ")
        if user_input in OPTIONS:
            if user_input.lower() == "q":
                clear()
                break
            elif user_input == "?":
                clear()
                Inputs().print_help()
            elif user_input == "+":
                clear()
                Inputs().add()
        else:
            print("*INVALID INPUT*")
