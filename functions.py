"""
Name: Ashish Panda
Description: Functions file
"""

try:
    from time import sleep
except ModuleNotFoundError:
    print("*IMPORT ERROR*")

def slow_text(variable, speed, spacing):
    """Creates slow text"""
    for characters in variable:
        sleep(speed)
        print(characters, end=spacing, flush=True)


def print_credits():
    """Displays the credits"""
    credits_heading = ("""
CREDITS
    """)
    credits_description = ("""
Bamboo Taskview
by Ashish Panda

  CS30-CAP_1
  2021-2022
    """)
    slow_text(credits_heading, 0.05, " ")
    print(credits_description)
