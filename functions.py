"""
Name: Ashish Panda
Description: Functions file
"""

try:
    from time import sleep
    from database import options
except ModuleNotFoundError:
    print("*IMPORT ERROR*")


def slow_text(variable, speed):
    """Creates slow text"""
    for characters in variable:
        sleep(speed)
        print(characters, end="", flush=True)


class inputs:
    """Stores all the input options"""

    def __init__(self):
        self.input = input

    def print_credits():
        """Displays the credits"""
        credits_heading = "\nC R E D I T S\n"
        credits_description = """
Bamboo Taskview
by Ashish Panda

CS30-CAP_1
2021-2022
        """
        slow_text(credits_heading, 0.06)
        print(credits_description)

    def print_help():
        """Displays all possible user inputs"""
        help_heading = "\nH E L P\n\n"
        slow_text(help_heading, 0.06)
        for option in options:
            for description in option:
                print(f"{description} {options[option]}")
