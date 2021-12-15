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


while True:
    Functions().clear()
    menu = input("""

[1] INPUT
[2] TASKVIEW
[3] CALENDAR

[C] CREDITS
[Q] QUIT

> """)

    if menu == "1":
        Functions().clear()
        input_loop()
    elif menu == "2":
        break
    elif menu == "3":
        break
    elif menu.lower() == "c":
        Functions().clear()
        Functions().print_credits()
        input("[PRESS ANY KEY TO GO BACK]")
    elif menu.lower() == "q":
        Functions().clear()
        sys.exit()
    else:
        Functions().clear()
        print("\n")
        print_invalid = ("*INVALID INPUT*")
        Functions().slow_text(print_invalid, 0.03)
