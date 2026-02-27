
#p042-precio-entrada-cine.py
#Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del cliente.

edad = int(input("Ingresa tu edad: "))

# Determinar el precio según la edad
if edad < 5:
    print("Tu entrada es gratis.")
elif edad <= 12:
    print("El precio de tu entrada es de $5.")
elif edad <= 64:
    print("El precio de tu entrada es de $10.")
else:
    print("El precio de tu entrada es de $7.")

print("\nPrograma terminado")

#-p042-precio-entrada-cine.py
# taquilla de un cine que determine el precio de una entrada según la edad 
# Menores de 5 años: Entran gratis.
# Niños (5 a 12 años): Pagan $5.
# Adultos (13 a 64 años): Pagan $10.
# Tercera edad (65 años o más): Pagan $7.

import os
os.system("cls")

print("--- Taquilla del Cine ---")

edad = int(input("Dame tu edad: "))

if edad < 5:
    print("Tu entrada es gratis.")
elif edad >= 5 and edad <= 12:
    print("El precio de tu entrada es de $5.")
elif edad >= 13 and edad <= 64:
    print("El precio de tu entrada es de $10.")
else:
    print("El precio de tu entrada es de $7.")
