import math
import time
import os
def distance(A,B):
    dx = A[0]-B[0]
    dy = A[1]-B[1]
    dz = A[2]-B[2]
    d = math.sqrt(dx**2+dy**2+dz**2)
    return d

A = []
B = []
play = True
while play:
    Apunkt1 = int(input("mata in x punkten i A : "))
    A.append(Apunkt1)
    Apunkt2 = int(input("\nmata in y punkten i A : "))
    A.append(Apunkt2)
    Apunkt3 = int(input("\nmata in z punkten i A : "))
    A.append(Apunkt3)
    Bpunkt1 = int(input("\n\nmata in x punkten i B : "))
    B.append(Bpunkt1)
    Bpunkt2 = int(input("m\nata in y punkten i B : "))
    B.append(Bpunkt2)
    Bpunkt3 = int(input("\nmata in z punkten i B : "))
    B.append(Bpunkt3)

    svar = distance(A,B)
    print (f"\nAnvståndet mellan {A} och {B} är : {svar:.2f}")
    time.sleep(1.5)
    A.clear()
    B.clear()
    again = input("Vill du stoppa? y/n : ").lower()
    if again == ("y"):
        break
    else:
        pass
