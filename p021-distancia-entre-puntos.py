#p021-distancia-entre-puntos.py
#Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano

import math

# punto A
x1 = float(input("Ingresa la coordenada x1 del punto A: "))
y1 = float(input("Ingresa la coordenada y1 del punto A: "))

# punto B
x2 = float(input("Ingresa la coordenada x2 del punto B: "))
y2 = float(input("Ingresa la coordenada y2 del punto B: "))

# Calcular la distancia
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre los puntos es:", d)