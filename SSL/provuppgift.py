import math
pi = math.pi

if input("Vill du mata in radie eller diameter? (r/d) : ").lower == "r":
    r = int(input("Vad är radien? (cm) : "))
else:
    r = int(input("Vad är diametern? (cm) : "))/2

o = r*2*pi
a = r*r*pi

print(f"Din cirkel har omkretsen {o:.2f} cm och arean {a:.2f} cm²")