#Native
import os.path
import subprocess
import sys
import shutil
import time

#PyPy
pyInstallerInstalled = True

try:
    import PyInstaller.__main__ as PyInstaller
except ImportError:
    pyInstallerInstalled = False

#Custom
from parse import Parser
from error import Error

version = "C- current interpreter version: 0.3.5"

class Interpreter:
    def Interpret(self, code : str) -> None:
        subprocess.call(["python", "output.py"])


def GetCode(filePath) -> str:
    if os.path.isfile(filePath):
        with open(filePath, 'r') as file:
            return file.read()
    else:
        Error("Input file not found")

def HandleArgs() -> None:
    if sys.argv[1] in ["--help", "-h"]:
        Error('''
        Command line arguments:
        --help -h: Prints this message
        --version -v: Prints the version of the interpreter
        --run -r (default) [file]: Runs the interpreter on the file specified
            ''')
    elif sys.argv[1] in ["--run", "-r"]:
        if len(sys.argv) < 3:
            Error("Invalid number of arguments")
        else:
            if os.path.isfile(sys.argv[2]):
                parser = Parser(GetCode((sys.argv[2])))
                def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
                def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
                def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
                prYellow("? Running code")
                if Exception == True:
                    prRed("✗ Code failed")
                    sys.exit(1)
                interpreter = Interpreter()
                interpreter.Interpret(parser.code)
                prGreen("✓ Job done successfully")
            else:
                Error("File not found")
    elif os.path.isfile(sys.argv[1]):
        parser = Parser(GetCode(sys.argv[1]))
        interpreter = Interpreter()
        interpreter.Interpret(parser.code)
        if len(sys.argv) < 3:
            Error("Invalid number of arguments")
        else:
            if os.path.isfile(sys.argv[2]):
                parser = Parser(GetCode((sys.argv[2])))
                fileName = sys.argv[3].split(".")[0]
                with open(f"{fileName}.py", "w") as f:
                    f.write(parser.code)
                    f.close()
            else:
                Error("File not found")
    elif sys.argv[1] in ["--version", "-v"]:
        print(version)
    else:
        Error("Invalid argument")

    if (os.path.isfile("output.py")):
        os.remove("output.py")

def CheckArgs() -> str:
    if len(sys.argv) < 2:
        Error("Invalid number of arguments")
    HandleArgs()
    
if __name__ == "__main__":
    CheckArgs()