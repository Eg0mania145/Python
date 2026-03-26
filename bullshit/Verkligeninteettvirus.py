import os
import time

os.system('cls')

play = True

print("Vi kommer ställa dig några ja eller nej frågor")
time.sleep(0.7)
print("skriv y för ja och n för nej")
time.sleep(0.7)
while play:
    Choice1 = input("Tillåter du att vi säljer din förstfödda till Vipeholm : \n").lower()
    if Choice1 in ("y", "yes") :
        time.sleep(0.7)
        
        Choice2 = input("tillåter du att vi säljer dina njurar till Försvarsmakten : \n").lower()
        if Choice2 in ("y", "yes"):
            time.sleep(0.7)
            Choice3 = input("tillåter du att vi säljer din ip adress till dörrsäljare : \n").lower()

            if Choice3 in ("y", "yes"):
                time.sleep(0.7)
                print ("tack för din hjälpsammhet")
                time.sleep(0.7)
                os.system('cls')
                play = False

            if Choice1 in ("n", "no"):
                print("fel svar, testa igen ")
                time.sleep(0.5)
                pass

        if Choice2 in ("n", "no"):
            print("fel svar, testa igen ")
            time.sleep(0.5)
            pass

    if Choice1 in ("n", "no"):
        print("fel svar, testa igen ")
        time.sleep(0.5)
        pass