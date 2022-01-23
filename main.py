"""
Name: Ashish Panda
Description: Input loop
"""

try:
    from functions import Inputs, Functions
    from database import OPTIONS
except ImportError:
    input("*IMPORT ERROR*\n")


def input_loop():
    """Main loop that user can interact with"""
    while True:
        print(f"\n// {Functions().opened_list()}")
        user_input = input("\n> ")
        if user_input in OPTIONS:
            if user_input.lower() == "q":
                Functions().clear()
                break
            elif user_input == "?":
                Functions().clear()
                Inputs().print_help()
            elif user_input == "+":
                Functions().clear()
                Inputs().add("")
            elif user_input == "*":
                Functions().clear()
                Inputs().add("quick")
            elif user_input == "/":
                Functions().clear()
                Inputs().access_list()
            elif user_input == "-":
                Functions().clear()
                Inputs().delete_item()
        else:
            print("*INVALID INPUT*")
