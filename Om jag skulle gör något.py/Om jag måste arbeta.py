import time
import os

os.system('cls')

nummmer = []
nummerskum = 0
play = True

kontroll = input("skriv ditt kontrolltal")
try:
    x = int(input("skriv in antalet tal du vill ha : ").strip())
    x += 1
    x -= 1
except:
    print("Skriv ett tal dumskalle!")
    exit(0)


while play:
    nummmer.append(input("skriv in dina tal"))
    nummerskum +=1
    if nummerskum == x:
        play = False
        nummmer.sort()
        print("talen som är större än ditt kontrolltal är : ")
        for i in nummmer:
            try:
                if int(i) > int(kontroll):
                    print(i)
                    time.sleep(2)
                    os.system('cls')
            except:
                print(f"{i} är inte ett tal")
    else:
        pass