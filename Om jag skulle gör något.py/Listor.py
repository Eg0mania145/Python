import os
os.system("cls;")


shopping_list = []
print("Avsluta inmatningen med \"stopp\"")
while True: 
    item = input("Mata in matvara: ")
    if item == "stopp": 
        break
    shopping_list.append(item) 
print("*** Shoppinglista ***")
sorted_shopping_list = sorted(shopping_list) #sortera shopping_list
for item in sorted_shopping_list: #använd len()-metoden för att ta reda på antalet element i listan
    print("***", item) #shopping_list[index] hämtar elementet i indexet index
print("*********************")
print("Totala antalet varor: ", len(sorted_shopping_list))