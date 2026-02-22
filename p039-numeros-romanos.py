#-p039-numero-romanos 
#-perdir al usuario un número entero entre 1 y 10 y muestre su equivalente en numeros romanos
# Si el número no esta en el rango solicitado que mande un mensaje de error

import os
os.system("cls")

print("Conversor de números arábigos a romanos (1-10)")

n = int(input("Introduce un número entero entre 1 y 10: "))

if n == 1:
    print("I")
elif n == 2:
    print("II")
elif n == 3:
    print("III")
elif n == 4:
    print("IV")
elif n == 5:
    print("V")
elif n == 6:
    print("VI")
elif n == 7:
    print("VII")
elif n == 8:
    print("VIII")
elif n == 9:
    print("IX")
elif n == 10:
    print("X")
else:
    print("Error: Número inválido.")

print("\nProceso terminado...")