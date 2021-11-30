"""
Name: Ashish Panda
Description: Main file
"""

try:
    from functions import inputs
    from database import options
except ModuleNotFoundError:
    print("*IMPORT ERROR*")

while True:
    user_input = input("\n> ")
    if user_input in options:
        try:
            if user_input == "?":
                inputs.print_help()
        except KeyError:
            print("*INVALID INPUT*")
            break
    else:
        print("*INVALID INPUT*")
        break