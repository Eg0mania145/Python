# Välja vad karaktären heter
# Välja mellan 5 objekt som kan hjälpa spelaren :Gun, Frying pan, Baby knife, stick that looks like sword, "Healing" powder 
# Möta en meth head som man måste ta sig förbi (om man väljer "Healing" powder kan man ge pulvret till methheaden för att komma förbi)
#i pinnen finns det ett svärd, ju mer det används desto mer av svärdet blir exposed efter 6 attacker blir svärdet helt exposed(gav upp på denna del)
#dictionary för inventory (typ fungerande)
#
#Till nästa lektion fixa valet av item och inventory och stats (stats blir jobbigt att göra)
import os
import time
os.system("clear")
money = 100
monster_health = 100
player_health = 100
inventory = {}

from listOfSlurs import worst_slurs

while player_health > 0:

    print("You walk in to a small town, directly after the gate a longbearded old man dressed in long robes")
    print("")
    print("Hey there!")
    name = input("What is your name fellow traveler?\n : ")
    if name in worst_slurs:
        import os
        print("get forked nerd")
        #while True:
           #os.fork() #fungerar men tar lång tid att starta datorn igen efter koden har körts
             
    else:
        pass
    print(f"Sick name {name}. *The old man daps you up*")
    print("The Old man offers you one item for free :")
    val = int(input("1)Gun \n2)Frying pan \n3)Baby knife \n4)Sword \n5)""Healing"" powder \n"))
    if val == 1:
        inventory['starting item'] = "gun"
    elif val == 2:
        inventory['starting item'] = "frying pan"
    elif val == 3:
        inventory['starting item'] = "baby knife"
    elif val == 4:
        inventory['starting item'] = "Sword"
    elif val == 5:
        inventory['starting item'] = "healing powder"
    elif val > 5:
        print("You have disrespected the old man, he stabs you with a knife, you bleed out on the ground")
        break
        player_health = 0
    if val <= 5:
            print(f"You have chosen {inventory['starting item']}")
    time.sleep(1.3)
    os.system("clear")
    print("You continue to walk through the town, on your way, you spot a store selling goods for tavelers.\n *you think 'perfect just what i need!'*")
    print("You enter the store, and the shopkeeper greets you...")
    time.sleep(1.3)
    print("Welcome to my store, what can i do for you?")
    print("1)Show me your goods \n2)Nothing, just looking around")
    val = int(input(": "))
    if val == 1:
        print("The shopkeeper shows you his goods, he has a variety of items that can help you on your journey")
        print("1)""Healing"" powder - 50 coins \n2)Sword - 100 coins \n3)gun - 100 \n4)Ammo for gun - 25 coins \n5)Nothing, just looking around")
        val = int(input("Which item do you want to buy? "))
        if val == 1:
            inventory['health potion'] = "health potion"
            print("You have bought a health potion")
            money -= 50
        elif val == 2:
            inventory['sword'] = "sword"
            print("You have bought a sword")
            money -= 100
        elif val == 3:
            inventory['gun'] = "gun"
            print("You have bought a gun")
            money -= 100
        elif val == 4:
            inventory['ammo for gun'] = int("10")
            print("You have bought ammo for your gun")
            money -= 25
        elif val == 5:
            print("you decide not to buy anything, the shopkeeper yells at you for wastin his time")
            money -= 20
        print(f"you now have {money} generic currency ")

    elif val == 2:
        print("You decide to just look around, the shopkeeper looks at you with a disappointed look")
        print("Shopkeeper: 'If you need anything, just let me know'")
    time.sleep(1.3)
    os.system("clear")
    print("You continue to walk through the town, on your way you spot a meth head, he looks at you with a crazy look in his eyes")
    print("Meth head: 'Hey you, you look like you have some money, can you spare some change?'")
    print("1)Give him some money \n2)Ignore him \n3)Give him your healing powder\n4)Attack him")
    val = int(input(": "))
    if val == 1:
        print("You give the meth head some money, he looks at you with a grateful look and walks away")
        money -= 10
    elif val == 2:
        print("You ignore the meth head, he gets angry and punches you, you take 16 damage")
        player_health -= 16
        time.sleep(1.3)
        val = int(input("1) Attack\n 2) Flee\n : "))
        if val == 1:
            choice = inventory['starting item']
            if choice == "gun" and inventory['ammo for gun'] > 0:
                print("you shoot the methhead in his head, he dies instantly")
                monster_health = 0
                inventory['ammo for gun'] -= 1
            elif choice == "sword":
                print("you attack the methhead with your sword, you chop his head off, he dies instantly")
                monster_health = 0
            elif choice == "frying pan":
                print("you attack the methhead with your frying pan, you hit him in the head, his skull caves in and he dies instantly")
                monster_health = 0
            elif choice == "baby knife":
                print("you attack the methhead with your baby knife, you stab him in the troat, he chokes on his own blood and sags to the ground, he dies slowly.")
                monster_health = 0
        elif val == 2:
            print("you try to flee, but the methhead is faster than you, he catches up to you and attacks you, you know have sepsis and take 84 damage")
            player_health -= 84
    elif val == 3:
        print("You give the meth head your healing powder, he looks at you with a grateful look, he puts a handful on his hand and snorts it, he looks at you with saliva bubbling from his mouth, he drops to the ground and starts to seize.")
        val = int(input("1) End his suffering\n2) Leave him be\n : "))
        if val == 1:
            if inventory['starting item'] == "gun" and inventory['ammo for gun'] > 0:
                print("you end the methheads suffering by shooting him in the head with your gun, he dies instantly")
                monster_health = 0
                inventory['ammo for gun'] -= 1
            elif inventory['starting item'] and inventory["ammo for gun"] == 0:
                print("you have no ammo left, you have to leave the methhead be, he continues to seize on the ground, after a while he stops seizing and dies on his own")
            elif inventory['starting item'] == "sword":
                print("you end the methheads suffering by chopping his head off with your sword, he dies instantly")
                monster_health = 0
            elif inventory['starting item'] == "frying pan":
                print("you end the methheads suffering by hitting him in the head with your frying pan, his skull caves in and he dies instantly")
                monster_health = 0
            elif inventory['starting item'] == "baby knife":
                print("you end the methheads suffering by stabbing him in the troat with your baby knife, he chokes on his own blood and sags to the ground.")
                monster_health = 0

        elif val == 2:
            print("you decide to leave the methhead be, he continues to seize on the ground, after a while he stops seizing and dies on his own")
            monster_health = 0
        inventory.pop('starting item')
    elif val == 4:
        print("you attack the methhead, he looks at you with a crazy look in his eyes, he attacks you back, you take 16 damage")
        player_health -= 16
        time.sleep(1.3)
        val = int(input("1) Attack\n 2) Flee\n : "))
        if val == 1:
            choice = inventory['starting item']
            if choice == "gun" and inventory['ammo for gun'] > 0:
                print("you shoot the methhead in his head, he dies instantly")
                monster_health = 0
                inventory['ammo for gun'] -= 1
            elif choice == "sword":
                print("you attack the methhead with your sword, you chop his head off, he dies instantly")
                monster_health = 0
            elif choice == "frying pan":
                print("you attack the methhead with your frying pan, you hit him in the head, his skull caves in and he dies instantly")
                monster_health = 0
            elif choice == "baby knife":
                print("you attack the methhead with your baby knife, you stab him in the troat, he chokes on his own blood and sags to the ground.")
                monster_health = 0
        elif val == 2:
            print("you try to flee, but the methhead is faster than you, he catches up to you and attacks you, you know have sepsis and take 84 damage")
            player_health -= 84
else:
    print("You have died, better luck next time!")
    os.system('clear')
   