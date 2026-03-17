import time
def skapa_konto(konton):
    konto_1 = input(" Vad ska kontot heta? : ")
    if konto_1 in konton:
        print("Kontot finns redan, försök igen")
        time.sleep(1)
    else:
        print("Kontot har skapats! ")
        konton[konto_1] = 0

def visa_saldo(konton):
    konto_2 = input("Vilket konto vill du se saldot på? : ")
    if konto_2 in konton:
        print(f"Saldot på {konto_2} är {konton[konto_2]}")
        time.sleep(1)
    else:
        print("Kontot finns inte, försök igen")
        time.sleep(1)
def sätt_in_pengar(konton):
    konto_3 = input("Vilket konto vill du sätta in pengar på? : ")
    if konto_3 in konton:
        summa = int(input("Hur mycket pengar vill du sätta in? : "))
        konton[konto_3] += summa
    else:
        print("Kontot finns inte, försök igen")
def main():
    konton = {}
    while True:
        print("\n1. Skapa ett konto: \n")
        print("2. Visa saldot på det specifka kontot: \n")
        print("3. Sätt in pengar på det specifika kontot: \n")
        print("4. Avsluta: \n")
        val = input("Välj ett alternativ : ")
        if val == ("1"):
            skapa_konto(konton)
        elif val == ("2"):
            visa_saldo(konton)
        elif val == ("3"):
            sätt_in_pengar(konton)
        elif val == ("4"):
            break
        else:
            print("Ogiltigt val, försök igen")

main()