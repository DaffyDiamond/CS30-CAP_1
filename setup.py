"""
Name: Ashish Panda
Description: Setup file
"""

from cx_Freeze import setup, Executable

executables = [
    Executable(
        "menu.py",
        targetName="Bamboo_Taskview.exe",
        icon="panda.ico"
        )
    ]

setup(
    name="Bamboo Taskview",
    version="1.0.0",
    description="Beta Release",
    executables=executables,
    options={"build_exe": {"include_files": ["HELP.md", "README.md"]}}
)
