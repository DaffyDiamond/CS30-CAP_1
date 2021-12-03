"""
Name: Ashish Panda
Description: Main menu
"""

# have this be the main directory (starting point)
# then be able to have options:
# - Input something
# - view tasks
#   - when in taskview, make it go to another menu which lists 
#     users own lists, automatically adding them there
# - calendar
# etc

try:
    import sys
    from functions import slow_text, clear
    from main import input_loop
except ModuleNotFoundError:
    print("*IMPORT ERROR*")

clear()

while True:
    menu = input("""

[1] INPUT
[2] TASKVIEW
[3] CALENDAR

[Q] QUIT

> """)

    if menu == "1":
        clear()
        input_loop()
    elif menu == "2":
        break
    elif menu == "3":
        break
    elif menu.lower() == "q":
        clear()
        sys.exit()
    else:
        clear()
        print("\n")
        print_invalid = ("*INVALID INPUT*")
        slow_text(print_invalid, 0.03)
