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

    def print_credits(self):
        """Displays the credits"""
        credits_heading = "\nC R E D I T S\n"
        credits_description = """
Bamboo Taskview
by Ashish Panda

CS30-CAP_1
2021-2022

Thank you for using my program :)
        """
        Functions().slow_text(credits_heading, 0.06)
        print(credits_description)

    def slow_text(self, variable, speed):
        """Creates slow text"""
        for characters in variable:
            sleep(speed)
            print(characters, end="", flush=True)

    def opened_list(self):
        """Check what the current list is"""
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

    def print_help(self):
        """Displays all possible user inputs"""
        help_heading = "\nH E L P\n\n"
        Functions().slow_text(help_heading, 0.06)
        for option in OPTIONS:
            print(option, OPTIONS[option])

    def add_priority(self):
        """User has option for priority level"""
        priorities = ["-", "#", "CHANGE TO ADD BOLDING!"]
        user_priority = input("PRIORITY\n'-' or '#'\n> ")
        if user_priority not in priorities:
            print("*INVALID INPUT*")
            self.add_priority()
        else:
            Functions().external(Functions().opened_list(), user_priority, item)

    def add(self, add_type):
        """User adds an item to their list (+)"""
        global item
        item = input("\n: ")
        if item.lower() == "q":
            return
        else:
            if add_type == "quick":
                Functions().external(Functions().opened_list(), "-", item)
            else:
                self.add_priority()

    def access_list(self):
        """Change current list opened"""
        global user_list
        user_list = input("\n>> ")
        with open("CS30-CAP_1/RESTRICTED_FILE.txt", "w") as f:
            f.write(user_list)

    def delete_item(self):
        """Deleting an item"""
        the_phrase = input(";")
        with open(f"{Functions().opened_list()}.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if the_phrase not in line:
                    f.write(line)
            f.truncate()

#   def modify_item(self):
