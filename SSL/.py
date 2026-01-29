# Skapa en tom lista
tal_lista = []

# Fråga efter tre tal och lägg dem i listan
for i in range(3):
    tal = int(input(f"Mata in tal {i+1}: "))
    tal_lista.append(tal)

# Skriv ut listan
print("Listan är:", tal_lista)

# Be användaren mata in ett tal som ska tas bort
ta_bort = int(input("Mata in ett tal som ska tas bort: "))

# Försök ta bort talet
if ta_bort in tal_lista:
    tal_lista.remove(ta_bort)
    print(f"{ta_bort} har tagits bort.")
else:
    print(f"{ta_bort} finns inte i listan.")

# Skriv ut den nya listan
print("Den nya listan är:", tal_lista)

