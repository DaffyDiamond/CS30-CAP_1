"""
Name: Ashish Panda
Description: Main menu
"""

try:
    import sys
    from functions import Functions
    from main import input_loop
except ImportError:
    input("*IMPORT ERROR*\n")

Functions().clear()

while True:
    menu = input("""
[1] INPUT
[2] TASKVIEW

[C] CREDITS
[Q] QUIT

> """)

    if menu == "1":
        Functions().clear()
        input_loop()
    elif menu == "2":
        Functions().clear()
        print(f"// {Functions().opened_list()}")
        with open(f"{Functions().opened_list()}.txt", "r") as f:
            print("\n" + f.read())
            input("\n\n[PRESS ANY KEY TO GO BACK]")
            Functions().clear()
    elif menu.lower() == "c":
        Functions().clear()
        Functions().print_credits()
        input("[PRESS ANY KEY TO GO BACK]")
    elif menu.lower() == "q":
        Functions().clear()
        sys.exit()
    else:
        Functions().clear()
        print("\n*INVALID INPUT*")
