
import os
import random
import time


play = True
again = None

lastInsult = ""
random_nummer = random.randint(1, 100)
timesNoWin = 0

insults = ["Din idiot!", "Fuck you!", "Jävla skit!", "Håll käften!", "Din jävla nolla!", "Jävla miffo", "Ditt absoluta ljushuvud", "Jävla pantskalle", "Ditt jävla lakristroll", "Kjoskmongo", "Du ser ut som om någon satte eld på ditt ansikte och försökte släcka det med en yxa.", "Gå och dö, ditt jävla slöseri av syre", "Jävla bortbyting"]
os.system("cls;")

def generateInsult() -> str:
    global lastInsult

    random.shuffle(insults)
    insult = insults[0]
    if insult == lastInsult:
        generateInsult()

    lastInsult = insult
    return insult

print("jag tänker på ett tal mellan 1 och 100 gissa vad det är")

while (play):
    timesNoWin = timesNoWin + 1
    nummer = int(input("Välj ett nummer mellan 1 och 100:"))

    os.system('cls')

    if(nummer) == random_nummer:
        print("Grattis! Du gissade rätt.")
        print(f"Det tog dig {timesNoWin} gånger att gissa rätt. {generateInsult()}" )
        timesNoWin = 0
        time.sleep(3)
        again = input("Vill du spela igen (y/n)").lower()
        if (again == "y"):
            os.system("cls;")
            random_nummer = random.randint(1, 100)
        else:
            play = False
            os.system("cls")
            print(f"Hejdå då ! {generateInsult()}")
    elif nummer > random_nummer:
        print (f"Nummret är mindre. {generateInsult()}")
    elif nummer < random_nummer:
        print (f"Nummret är större. {generateInsult()} ")