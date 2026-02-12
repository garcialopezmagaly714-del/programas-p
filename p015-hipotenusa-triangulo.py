# p015-hipotenusa-triangulo.py
#calcule la longitud de la hipotenusa de un triángulo rectángulo

import math


longlado1 = float(input("Ingresa la longitud del primer cateto: "))
longlado2 = float(input("Ingresa la longitud del segundo cateto: "))

# Calcular la hipotenusa
hipotenusa = math.sqrt(longlado1 * longlado1 + longlado2 * longlado2)

print("La longitud de la hipotenusa es:", hipotenusa)