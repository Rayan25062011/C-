# Created on iPad

import os.path
import subprocess
import sys
import shutil


pyInstallerInstalled = True

try:
    import PyInstaller.__main__ as PyInstaller
except ImportError:
    pyInstallerInstalled = False


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
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        Error('''
        Command line arguments:
        --help -h: Prints this message
        --version -v: Prints the version of the interpreter
        --run -r (default) [file]: Runs the interpreter on the file specified
            ''')
    elif sys.argv[1] == "--run" or sys.argv[1] == "-r":
        if len(sys.argv) < 3:
            Error("Invalid number of arguments")
        else:
            if os.path.isfile(sys.argv[2]):
                parser = Parser(GetCode((sys.argv[2])))
                interpreter = Interpreter()
                interpreter.Interpret(parser.code)
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
                with open(fileName + ".py", "w") as f:
                    f.write(parser.code)
                    f.close()
            else:
                Error("File not found")
    elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
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
