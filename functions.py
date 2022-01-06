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

    def external(self, the_list, the_item, read):
        """External file handling for list items"""
        with open(f"{the_list}.txt", "a") as f:
            f.write(f"\n{the_item}")
        with open(f"{the_list}.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if not len(line) < 2:
                    f.write(line)
            f.truncate()
        if read == "r":
            with open(f"{the_list}.txt", "r+") as f:
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
        priorities = ["bold", "clear"]
        for f in priorities:
            print(f)
        bold = "\033[1m"
        end_font = "\033[0m"
        user_priority = input("\n! ")
        if user_priority not in priorities:
            if user_priority.lower() == "q":
                return
            print("*INVALID INPUT*")
            self.add_priority()
        else:
            if user_priority.lower() == "bold":
                p_item = bold + item + end_font
            elif user_priority.lower() == "clear":
                p_item = end_font + item + end_font
            Functions().external(
                Functions().opened_list(), 
                p_item, "r"
                    )

    def add(self, add_type):
        """User adds an item to their list (+)"""
        global item
        item = input("\n: ")
        item = "- " + item
        if item.lower() == "q":
            return
        else:
            Functions().external(
                Functions().opened_list()+"COPY",
                item, "")
            if add_type == "quick":
                Functions().external(
                    Functions().opened_list(),
                    item, "r")
            else:
                self.add_priority()

    def access_list(self):
        """Change current list opened"""
        global user_list
        user_list = input("\n>> ")
        with open("CS30-CAP_1/RESTRICTED_FILE.txt", "w") as f:
            f.write(user_list)

    def modify_item(self, how_modify):
        """Modifying an item"""
        with open(f"{Functions().opened_list()}COPY.txt", "r+") as f:
            line_offset = []
            offset = 0
            lines = f.readlines()
            f.seek(0)
            counter = 0
            for line in lines:
                line_offset.append(offset)
                offset += len(line)+1
            for x in line_offset:
                f.seek(x)
                counter += 1
                f.write(str(counter))
        with open(f"{Functions().opened_list()}COPY.txt", "r+") as f:
            print(f.read())
        line_number = input("\n# ")

        if line_number.lower() == "q":
            return

        elif how_modify == "delete":
            with open(f"{Functions().opened_list()}COPY.txt", "r+") as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if not line.startswith(f"{line_number}"):
                        f.write(line)
                f.truncate()
            with open(f"{Functions().opened_list()}.txt", "r+") as f:
                line_offset = []
                offset = 0
                lines = f.readlines()
                f.seek(0)
                counter = 0
                for line in lines:
                    line_offset.append(offset)
                    offset += len(line)+1
                for x in line_offset:
                    f.seek(x)
                    counter += 1
                    f.write(str(counter))
            with open(f"{Functions().opened_list()}.txt", "r+") as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if not line.startswith(f"{line_number}"):
                        f.write(line)
                f.truncate()
            with open(f"{Functions().opened_list()}COPY.txt", "r+") as f:
                line_offset = []
                offset = 0
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    line_offset.append(offset)
                    offset += len(line)+1
                for x in line_offset:
                    f.seek(x)
                    f.write("-")
            with open(f"{Functions().opened_list()}.txt", "r+") as f:
                line_offset = []
                offset = 0
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    line_offset.append(offset)
                    offset += len(line)+1
                for x in line_offset:
                    f.seek(x)
                    f.write("-")
            with open(f"{Functions().opened_list()}.txt", "r+") as f:    
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if not line.startswith("-["):
                        f.write(line)
                    else:
                        line = line[:0] + "\033" + line[1:]
                        f.write(line)
            with open(f"{Functions().opened_list()}.txt", "r+") as f:
                print(f.read())
        
        elif how_modify == "modify":
            print("soonTM")


#   def modify_item(self):
#   due dates
