import os
import time

os.system('cls')


text = input("Skriv in en textsträng : ").strip()
bokstav = input("Vilken bokstav vill du ta bort? : ").strip()

time.sleep(1)
os.system('cls')


if len(bokstav) != 1:
    print("Du måste skriva exakt EN bokstav!")
    exit(0)



nytext = text.replace(bokstav, "").replace(bokstav.upper(), "")


print("\nResultatet blir : ")
print(nytext)


time.sleep(1)
os.system('cls')