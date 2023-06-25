import os
import json
import platform
import sys

def printMainMessage(mes):
    print(f"\033[38;5;231m{mes}\033[38;5;231m")


def printErrorMessage(mes):
    print(f"\033[38;5;196m{mes}\033[38;5;231m")


def printWarnMessage(mes):
    print(f"\033[38;5;214m{mes}\033[38;5;231m")

def createInput(question):
    printMainMessage("- System Question -")
    printMainMessage(question)
    res = input(">> ")
    return res


def whichPythonCommand():
    LocalMachineOS = platform.system()
    if (
        LocalMachineOS == "win32"
        or LocalMachineOS == "win64"
        or LocalMachineOS == "Windows"
    ):
        return "python"
    else:
        return "python3"
    
printMainMessage("----------")
printMainMessage("Mewt Customizer - v1.0 beta")
printMainMessage("Made by efazdev")

def themeEditor():
    printMainMessage("Theme Creator")
    print("----------")
    os.system(f"{whichPythonCommand()} mewtThemeApplier.py main.py {createInput('RGB Color (R)')} {createInput('RGB Color (G)')} {createInput('RGB Color (B)')} 5 {createInput('Hex Color (no # symbol)')} {createInput('Hex Start Gradient Color (no # symbol)')} {createInput('Hex End Gradient Color (no # symbol)')}")
    main()

def versionEditor():
    printMainMessage("Version Editor")
    print("----------")
    os.system(f"{whichPythonCommand()} versionEditor.py main.py '{createInput('Old Version?')}' '{createInput('New Version?')}'")
    main()

def main():
    printMainMessage("----------")
    printMainMessage("Selection Available:")
    printMainMessage("1 - Theme Creator")
    printMainMessage("2 - Version Editor")
    printMainMessage("----------")
    main_input = input(">> ")
    if main_input == "1":
        themeEditor()
    elif main_input == "2":
        versionEditor()
    else:
        printErrorMessage("Error, Not Found (404)")
        main()
main()