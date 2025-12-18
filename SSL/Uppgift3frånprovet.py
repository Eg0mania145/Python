antal_sidor = int(input("mata in antal sidor"))
omkrets = 0
for i in range(antal_sidor):
    sida = float(input(f"mata in sida {i+1} : "))
    omkrets = omkrets + sida
print("resultat:")
print(f"Omkresten för {antal_sidor}-hörning blir :{omkrets}")