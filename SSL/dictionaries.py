# skapa en dictionary med månader och deras nummer
# input Skriv in en dag
# input Skriv in en månad i textform
# gör om månad till siffra
# input Skriv in ett år
# output skriv ut i sifferform

dict_månader =  {
    "januari" : "01",
    "februari" : "02",
    "mars" : "03",
    "april" : "04",
    "maj" : "05",
    "juni" : "06",
    "juli" : "07",
    "augusti" : "08",
    "september" : "09",
    "oktober" : "10",
    "november" : "11",
    "december" : "12"
}
dag = input("skriv in en dag : ")
månader = input("skriv in månaden : ").lower()

månad = dict_månader[månader]
år = input("skriv in året : ")

print(f"{år}-{månad}-{dag}")