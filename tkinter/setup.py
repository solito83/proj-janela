# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# SimpleTkApp.py is a very simple type of Tkinter application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application
# python setup.py build

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("jan-001.py", base=base)]

setup(
    name="ferramentas",
    version="0.1",
    description="Controle de ferramentas",
    executables=executables,
)
