import sys
from cx_Freeze import setup, Executable

#includefiles = {['thumbnail.PNG','selected.PNG','introscreen.PNG','chars12x16/','chars6x8/']

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "ChadTech",
        version = "0.30",
        description = "ChadTech that does text",
        options = {"build_exe": build_exe_options},
        executables = [Executable("ChadTech.py", base=base,icon="thumbnail.ICO")])