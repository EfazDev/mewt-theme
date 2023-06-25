import json
import colorama
from colorama import Fore, Style
import ast
import os

mewtMain = ""
r = 0
g = 0
b = 0
i = 0
hexcode = ""

hexcodestart = ""
hexcodeend = ""

# File Asked Step

print("Welcome to Mewt Sniper Theme Customizer!")
print("Change embeds, global log embed color and your main theme in mewt UI!")
print("Made by efazdev")

print("----------")

print("File Stage")

def promptMain():
    global mewtMain
    asked = input("What's your mewt sniper main.py?")
    asked = asked.replace("'", "")
    correct = input("This is correct? If not, enter n.")
    if correct.lower() == "y":
        mewtMain = asked
    else:
        promptMain()
promptMain()

print("----------")

# Color Variable Preparation

print("Color Stage")

def rgbStage():
    rval = input("Enter your RGB (R): ")
    gval = input("Enter your RGB (G): ")
    bval = input("Enter your RGB (B): ")
    ival = input("Enter your Index (Resource usable to choose from: https://static.javatpoint.com/python/images/how-to-print-colored-text-in-python2.png): ")
    hex = input("Enter Hex Code for Color (no # symbol): ")

    hexstart = input("Enter Gradient Hex Code for Color (no # symbol) (start): ")
    hexend = input("Enter Gradient Hex Code for Color (no # symbol) (end): ")

    rval2 = int(rval)
    gval2 = int(gval)
    bval2 = int(bval)
    ival2 = int(ival)

    if rval2 and bval2 and gval2 and hex and hexstart and hexend:
        print(f"RGB: \x1b[38;2;{str(rval2)};{str(gval2)};{str(bval2)}mTest Message{Style.BRIGHT}{Fore.WHITE}")
        print(f"Index: \033[1;{str(ival2)}mTest Message{Style.BRIGHT}{Fore.WHITE}")
        c = input(f"Confirm? (y/n): ")
        if c.lower() == "y":
            global r
            global g
            global b
            global i
            r = rval2
            g = gval2
            b = bval2
            i = ival2
            global hexcode
            hexcode = hex.upper()

            global hexcodestart
            global hexcodeend
            hexcodestart = hexstart.upper()
            hexcodeend = hexend.upper()
        else:
            rgbStage()
    else:
        print(f"Error: An variable was inputted correctly and no number was returned. receieved: {str(rval2)}, {str(gval2)}, {str(bval2)}, {hex}, {hexstart}, {hexend}")
        rgbStage()
rgbStage()

# Code Prepared

print("----------")

print("Finishing few changes..")

rawMewt = open("mewtRaw.txt", "r")
contents = rawMewt.read()
a = contents.replace("(((formatmess_mewtstyle)))", f'f"\\x1b[38;2;{str(r)};{str(g)};{str(b)}m"')
c = a.replace("(((formatmess_hex)))", "0x" + hexcode)
d = c.replace("(((formatmess_decimal)))", str(ast.literal_eval("0x" + hexcode)))

d = d.replace("(((formatmess_hexstart)))", "0x" + hexcodestart)
d = d.replace("(((formatmess_hexend)))", "0x" + hexcodeend)

e = d.replace("4.4.4 Tester Version 2", "4.4.4 Tester Version 2 - Theme Applier (By efazdev)")

print("Code is ready!")

applynow = input("Apply now to file? ")
if applynow.lower() == "y":
    f = open(mewtMain, "w")
    print("Opened")
    f.write(e)
    f.close()
    print("Finished process and overwrited the script.")
    print(f"Overwrited: {mewtMain}")
print("Script finished")