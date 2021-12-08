"""
Name: Ashish Panda
Description: Functions file
"""

try:
    from time import sleep
    from database import OPTIONS
    from os import system, name
except ModuleNotFoundError:
    print("*IMPORT ERROR*")


def clear():
    """Clears the console"""
    if name == "nt":
        system("cls")
    else:
        system("clear")


def slow_text(variable, speed):
    """Creates slow text"""
    for characters in variable:
        sleep(speed)
        print(characters, end="", flush=True)


def external(priority, item):
    with open("list.txt", "a") as f:
        f.write(f"\n{priority} {item}")
    f = open("list.txt", "r")
    print(f.read())


class Inputs:
    """Stores all the input options"""
    def print_credits(self):
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

    def print_help(self):
        """Displays all possible user inputs"""
        help_heading = "\nH E L P\n\n"
        slow_text(help_heading, 0.06)
        for option in OPTIONS:
            for description in option:
                print(f"{description} {OPTIONS[option]}")

    def add_priority(self):
        priorities = ["-", "#"]
        user_priority = input("PRIORITY\n'-' or '#'\n> ")
        if user_priority not in priorities:
            print("*INVALID INPUT*")
            self.add_priority()
        else:
            external(user_priority, item)

    def add(self):
        """User adds an item to their list (+)"""
        global item
        item = input("\n: ")
        self.add_priority()

#    def quick_add(self):
#        """User adds an item to their list (++)"""
