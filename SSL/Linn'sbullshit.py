namn1 = input("skriv in första namnet : ")
namn2 = input("skriv in andra namnet : ")

if len(namn1) > len(namn2):
    print(f"{namn1} är längre än {namn2}, den har {len(namn1)} bokstäver")
elif len(namn2) > len(namn1):
    print(f"{namn2} är längre än {namn1}, den har {len(namn2)} bokstäver")
else:
    print (f"Båda namn är lika stora, de har {len(namn1)} bokstäver")