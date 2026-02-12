x = 0

print("om du vill stoppa skriv stopp")
namn = []
play = True
while play == True:
    x = x+1
    A =input(f"skriv in namn {x} : ").lower()
    namn.append(A)
    if A == "stopp":
        namn.remove("stopp")
        namn.sort(key = len)
        print (namn)
        break





