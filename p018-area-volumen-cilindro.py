#p018-area-volumen-cilindro.py
#Crea un programa que calcule el área y volumen de un cilindro

import math

R = float(input("Ingresa el radio del cilindro: "))
h = float(input("Ingresa la altura del cilindro: "))

Area = 2 * math.pi * R * (R + h)
Volumen = math.pi * (R ** 2) * h

print("El área del cilindro es:", Area)
print("El volumen del cilindro es:", Volumen)