#-p037-numero-mayor
import os

def mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

# Principal
os.system("cls")
n1 = int(input("Ingresa el 1er número: "))
n2 = int(input("Ingresa el 2do número: "))
n3 = int(input("Ingresa el 3er número: "))
r = mayor(n1, n2, n3)

print("El mayor es", r)