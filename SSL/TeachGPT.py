ord = str(input("Skriv in ordet : "))
gräns = float(input("Vad är gränsen : "))

if len(ord) > gräns:
    print(f"Långt ord. Ordet har {len(ord)-int(gräns)} tecken mer än gränsen")
elif len(ord) < gräns:
    print(f"Kort ord. Ordet har {gräns - int(len(ord))} tecken mer än gränsen")
else:
    print("Ditt ord är lika långt som gränsen")