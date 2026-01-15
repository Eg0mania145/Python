import random
import time
import os

os.system('cls')

class Tarningsspel:
    def __init__(self):
        self.poäng = 0
        self.runda = 0

    def kasta_tarning(self):
        return random.randint(1, 6)

    def spel(self):
        print("Vill du spela mitt tärningspel?")
        time.sleep(0.7)
        while True:
            svar = input("Vill du kasta tärningen? (y/n) : ").lower().strip()
            if svar == ("y"):
                tärning = self.kasta_tarning()
                print(f"Du kastade en {tärning}!")
                self.poäng += tärning
                self.runda += 1
                print(f"Du har nu {self.poäng} poäng efter {self.runda} runda/rundor")
                time.sleep(1.5)
            elif svar == ("n"):
                print("Spelet avslutas")
                break
            else:
                print("Felaktig inmatning. försök igen")

        print(f"\nSlutpoäng: {self.poäng} poäng efter {self.runda} runda/rundor")

    def statistik(self):
        print("\nStatistik:")
        print(f"Genomsnittspoäng per runda : {self.poäng / self.runda:.2f}")
        print(f"Högsta poäng under en runda : {max([self.kasta_tarning() for _ in range(self.runda)])}")
        time.sleep(2)
        os.system('cls')

def huvudprogram():
    spel = Tarningsspel()
    spel.spel()
    spel.statistik()

if __name__ == "__main__":
    huvudprogram()