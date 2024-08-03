import random as random

print("¡Intenta adivinar mi número!")
x = random.randrange(1,10)
a = int(input("Elige un número del 1 al 10..."))
if a == x:
    print("¡Correcto!")
else:
    while a != x:
        print("Lo siento, te has equivocado.")
        a = int(input("Intenta de nuevo. Elige un número del 1 al 10..."))
        if a == x:
            print("¡Correcto!")

        

