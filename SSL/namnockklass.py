import os
import time

os.system('cls')


play = False

listofnames = []
listofclass = []

print("Avsluta inmatningen med \"stopp\"")
time.sleep(1)
while play == False :

    namn = str(input("vad heter du? : ")).lower()
    if namn == ("stopp"):
        os.system("cls")
        print("--NAMN---Klass--")
        for namn, klas in zip(listofnames, listofclass):
            print(f"{namn} | {klas}" )
            time.sleep(0.5)
        time.sleep(7)
        os.system('cls')
        break
    klass = str(input("vilken klass går du i? : ")).lower()

    listofnames.append(namn)
    listofclass.append(klass)
    if namn!= ("stopp"):
        pass