
import os
import random
import time


play = True
again = None

timesNoWin = 0

insults = ["Din idiot!", "Fuck you!", "Jävla skit!", "Håll käften!", "Din jävla nolla!", "Jävla miffo", "Ditt absoluta ljushuvud", "Jävla pantskalle", "Ditt jävla lakristroll", "Kjoskmongo", "Du ser ut som om någon satte eld på ditt ansikte och försökte släcka det med en yxa.", "Gå och dö, ditt jävla slöseri av syre", "Jävla bortbyting"]
os.system("cls;")



while (play):
    timesNoWin = timesNoWin + 1
    random_nummer = random.randint(1, 6)
    nummer = input("Välj ett nummer mellan 1 och 6: ")
    if int(nummer) == random_nummer:
        print("Grattis! Du gissade rätt.")
        print(f"Det tog dig {timesNoWin} gånger att gissa rätt" )
        timesNoWin = 0
        again = input("Vill du spela igen (y/n)").lower()
        if (again == "y"):
            pass
            os.system("cls;")
        else:
            play = False
    else:
        currentInsultNum = random.randint(0, len(insults))
        currentInsult = insults[currentInsultNum - 1]
        os.system("cls;")
        print(f"{currentInsult}\nNummret var {random_nummer}")
        currentInsultNum = random.randint(0, len(insults))
        currentInsult = insults[currentInsultNum]
        print(f"Du har gissat {timesNoWin} gånger utan att ha rätt. {currentInsult} ")
        time.sleep(4)
        os.system("cls;")
        again = input("Vill du spela igen (y/n)").lower()
        if (again == "y"):
            pass
            os.system("cls;")
        else:
            play = False
        
        