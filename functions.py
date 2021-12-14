"""
Name: Ashish Panda
Description: Functions file
"""

try:
    from time import sleep
    from database import OPTIONS
    from os import system, name
except ImportError:
    input("*IMPORT ERROR*\n")


class Functions:
    """Stores general functions"""

    def slow_text(self, variable, speed):
        """Creates slow text"""
        for characters in variable:
            sleep(speed)
            print(characters, end="", flush=True)

    def opened_list(self, option):
        if option == "//":
            with open("CS30-CAP_1/RESTRICTED_FILE.txt", "r") as f:
                print(f"\n// {f.read()}")
        else:
            with open("CS30-CAP_1/RESTRICTED_FILE.txt", "r") as f:
                return f.read()

    def external(self, the_list, the_priority, the_item):
        """External file handling for list items"""
        with open(f"{the_list}.txt", "a") as f:
            f.write(f"\n{the_priority} {the_item}")
        f = open(f"{the_list}.txt", "r")
        print(f.read())

    def clear(self):
        """Clears the console"""
        if name == "nt":
            system("cls")
        else:
            system("clear")


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
        Functions().slow_text(credits_heading, 0.06)
        print(credits_description)

    def print_help(self):
        """Displays all possible user inputs"""
        help_heading = "\nH E L P\n\n"
        Functions().slow_text(help_heading, 0.06)
        for option in OPTIONS:
            for description in option:
                print(f"{description} {OPTIONS[option]}")

    def add_priority(self):
        """User has option for priority level"""
        priorities = ["-", "#"]
        user_priority = input("PRIORITY\n'-' or '#'\n> ")
        if user_priority not in priorities:
            print("*INVALID INPUT*")
            self.add_priority()
        else:
            Functions().external(Functions().opened_list(""), user_priority, item)

    def add(self):
        """User adds an item to their list (+)"""
        global item
        item = input("\n: ")
        self.add_priority()

    def access_list(self):
        global user_list
        user_list = input("\n>> ")
        with open("CS30-CAP_1/RESTRICTED_FILE.txt", "w") as f:
            f.write(user_list)

#    def quick_add(self):
#        """User adds an item to their list (++)"""
