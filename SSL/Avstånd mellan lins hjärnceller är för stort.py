import math
import time

A = []
B = []

def distance(A,B):
    dx = A[0]-B[0]
    dy = A[1]-B[1]
    dz = A[2]-B[2]
    d = math.sqrt(dx**2+dy**2+dz**2)
    return d

play = True

while play:
    xyzförA = input("Mata in X, Y och Z punkten för A med mellanslag mellan varje punkt : ") 
    A = list(map(int,xyzförA.split()))
    
    xyzförB = input("Mata in X, Y och Z punkten för B med mellanslag mellan varje punkt : ") 
    B = list(map(int,xyzförB.split()))

    svar = distance(A,B)
    print (f"\nAnvståndet mellan {A} och {B} är : {svar:.2f}")
    time.sleep(1)
    A.clear()
    B.clear()
    again = input("Vill du stoppa? y/n : ").lower()
    if again == ("y"):
        break
    else:
        pass
