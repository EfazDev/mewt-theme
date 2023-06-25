import os
import sys

mewtMain = ""
versionOld = ""
version = ""

def validateArguments():
    listOfArgs = sys.argv
    if len(listOfArgs) >= 2:
        global mewtMain
        mewtMain = listOfArgs[1]
        global versionOld
        versionOld = listOfArgs[2]
        global version
        version = listOfArgs[3]
        return True
    else:
        return False

validateArgs = validateArguments()
if validateArgs == False:
    # File Asked Step

    print("Welcome to Mewt Sniper Version Editor!")
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

    # Code Prepared

    print("----------")

    print("Main Stage")

    def promptVersion():
        global version
        global versionOld
        asked2 = input("What's your old version?")
        asked = input("What's your new version?")
        correct = input("This is correct? If not, enter n.")
        if correct.lower() == "y":
            version = asked
            versionOld = asked2
        else:
            promptVersion()
    promptVersion()

    print("Finishing few changes..")

rawMewt = open(mewtMain, "r")
contents = rawMewt.read()
e = contents.replace(versionOld, version)

print("Code is ready!")
if validateArgs == False:
    applynow = input("Apply now to file? ")
    if applynow.lower() == "y":
        f = open(mewtMain, "w")
        print("Opened")
        f.write(e)
        f.close()
        print("Finished process and overwrited the script.")
        print(f"Overwrited: {mewtMain}")
else:
    f = open(mewtMain, "w")
    print("Opened")
    f.write(e)
    f.close()
    print("Finished process and overwrited the script.")
    print(f"Overwrited: {mewtMain}")
