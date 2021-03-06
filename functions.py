"""
Name: Ashish Panda
Description: Functions file
"""

try:
    from database import OPTIONS
    from os import system, name
except ImportError:
    input("*IMPORT ERROR*\n")


class Functions:
    """Stores general functions"""

    def print_about(self):
        """Displays the credits"""
        print("""
A B O U T

Bamboo Taskview
by Ashish Panda

v1.0.0
CS30-CAP_1
2021-2022

Icon created by:
Freepik from flaticon.com

Thank you for using my program :)
        """)

    def opened_list(self):
        """Check what the current list is"""
        try:
            with open("RESTRICTED_FILE.txt", "r") as f:
                return f.read()
        except:
            return "list"

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
        print("\nO P T I O N S\n")
        for option in OPTIONS:
            print(option, OPTIONS[option])

    def add(self, add_type):
        """User adds an item to their list (+)"""
        print("\nA D D")
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
                Functions().clear()
                self.add_priority()

    def add_priority(self):
        """User has option for priority level"""
        print("""\nP R I O R I T Y\n
[1] NORMAL
[2] BOLD
        """)
        global item
        bold = "\033[1m"
        end_font = "\033[0m"
        user_priority = input("\n! ")
        if user_priority.lower() == "q":
            return
        elif user_priority == "1":
            None
        elif user_priority == "2":
            item = bold + item + end_font
        else:
            Functions().clear()
            print("\n*INVALID INPUT*")
            self.add_priority()  # recursion
        Functions().external(
            Functions().opened_list(),
            item, "r"
                )

    def access_list(self):
        """Change current list opened"""
        global user_list
        user_list = input("\n>> ")
        with open("RESTRICTED_FILE.txt", "w") as f:
            f.write(user_list)

    def delete_item(self):
        """Deleting an item"""

        def list_functions(the_function):
            """Efficiently used when deleting items"""
            for x in range(2):
                if x == 0:
                    the_list = f"{Functions().opened_list()}COPY"
                else:
                    the_list = Functions().opened_list()
                if the_function == "number":
                    with open(f"{the_list}.txt", "r+") as f:
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
                elif the_function == "delete":
                    with open(f"{the_list}.txt", "r+") as f:
                        lines = f.readlines()
                        f.seek(0)
                        for line in lines:
                            if not line.startswith(f"{line_number}"):
                                f.write(line)
                        f.truncate()
                elif the_function == "replace":
                    with open(f"{the_list}.txt", "r+") as f:
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

        # List is numbered by line
        list_functions("number")
        with open(f"{Functions().opened_list()}COPY.txt", "r+") as f:
            print("\n" + f.read())
        # User selects line to delete
        line_number = input("\n# ")
        # User can go back instead of proceeding
        if line_number.lower() == "q":
            return
        # Line selected is deleted
        list_functions("delete")
        list_functions("replace")
        # Handles bolded tasks
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
            print("\n" + f.read())
