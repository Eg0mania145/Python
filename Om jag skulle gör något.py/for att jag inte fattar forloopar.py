import os
import time

os.system("cls;")

play = True
again = None

timesplayed = 0
listofnumbers = []
positions = []
print("skriv in vilka tal du vill använda som övre och under gräns")

tal1 = int(input("skriv in första talet\n"))
tal2 = int(input("skriv in andra talet\n"))
os.system("cls;")

while (play):
    timesplayed = timesplayed + 1
    tal3 = int(input("skriv in det tal du vill titta var det är\n "))
    talmitten = (int(tal1 + tal2) * 0.5)
    listofnumbers.append(tal3)
    listofnumbers.sort()

    if tal3 < tal1:
        pos = "ute till vänster"
    elif tal3 > tal2:
        pos = "ute till höger"
    elif tal3 == talmitten:
        pos = "exakt i mitten"
    elif tal1 < tal3 < talmitten:
        pos = "mellan vänstra gränsen och mitten"
    elif talmitten < tal3 < tal2:
        pos = "mellan mitten och högra gränsen"
    elif tal3 == tal1:
        pos = "på vänstra gränsen"
    elif tal3 == tal2:
        pos = "på högra gränsen"
    
    os.system("cls;")
    positions.append(pos)

    if tal3 == 69 or tal3 == 420 or tal3 == 67:
        play =False
        print("ha ha så roligt jävla 5åring")
        time.sleep(3)
        os.system("cls;")
    
    
    else:

        print(f"Talet {tal3} är {pos}")
        again = input("Vill du skriva in ett annat tal (y/n)").lower()
        if (again == "y"):
            pass
    
        else:
            play = False
            print(f"du tittade på {timesplayed} tal")
            print("Talen och deras positioner:")
            for number, pos in zip(listofnumbers, positions):
                print(f"Talet {number} var {pos}")
                time.sleep(1)
            time.sleep(5)
            os.system("cls;")
