

print ("god morgon ")
name1 = input ("vad heter du? ")
name2 = input ("vad heter du i efternamn? ")



age = input ("hur gammal fyller du i år? ")
Month = input ("vilken månad är du född? ")
Date = input ("och vilket datum? ")
Year = None
currentDate = (2025)
ageINT= int(age)
year = currentDate - int(age)
print (f"hej på dig {name1} {name2}! Du är {age} år gammal och är född den {Date}:e {Month} år {year}! Stämmer detta?")
stammer = input("-> (y/n) : ")

if (stammer == "y" or stammer == "Y"):
    print("Lessgoooo ja e bäst")
else:
    print ("Na fuck you bruh")