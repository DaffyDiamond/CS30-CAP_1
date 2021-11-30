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
    user_input = input("> ")
    # if user_input in options:
        # try:
            # if user_input == "?":
                # inputs.help
        # except some error:
            # print(f"*INVALID INPUT* \n{inputs.help}")
    # else:
        # print(f"*INVALID INPUT* \n{inputs.help}")