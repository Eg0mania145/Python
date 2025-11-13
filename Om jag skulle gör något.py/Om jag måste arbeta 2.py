import os
import time

os.system('cls')
text = []
nytext = " "
bokstav = []
play = True
again = None

while play == True:
    text = input("Skriv in en textsträng med små bokstäver : ").strip().lower()
    bokstav = input("Vilken bokstav vill du ta bort? : ").strip().lower()

    time.sleep(1)
    os.system('cls')


    if len(bokstav) != 1:
        print("Du måste skriva exakt EN bokstav!")
        exit(0)


    nytext = " "
    for char in text:
        if char != bokstav:
            nytext += char


    print("\nResultatet blir : ")
    print(nytext)
    if input("vill du köra igen : ").lower() == ("n") :
        break
    else:
        pass


    time.sleep(1)
    os.system('cls')