"""
Name: Ashish Panda
Description: Setup file
"""

from cx_Freeze import setup, Executable

executables = [Executable("menu.py")]

setup(
    name="Bamboo Taskview",
    version="0.3.0",
    description="Beta Release",
    executables=executables,
)
