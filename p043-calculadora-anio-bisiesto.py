
#p043-calculadora-anio-bisiesto.py
#Escribe un programa que determine si un año, ingresado por el usuario, es bisiesto.


anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0):
    print(f"El año {anio} es bisiesto. (Porque es divisible por 4 pero no por 100).")
elif (anio % 400 == 0):
    print(f"El año {anio} es bisiesto. (Porque es divisible por 400).")
else:
    if anio % 100 == 0:
        print(f"El año {anio} no es bisiesto. (Porque es divisible por 100 pero no por 400).")
    else:
        print(f"El año {anio} no es bisiesto. (Porque no es divisible por 4).")

# -p043-calculadora-año-bisiesto.py 
# determinar si un año, ingresado por el usuario, es bisiesto. Un año es bisiesto
# si cumple una de las siguientes condiciones:
# 1. Es divisible por 4, pero no es divisible por 100.
# 2. Es divisible por 400.

import os
os.system("cls")

print("--- Verificador de Años Bisiestos ---")

año = int(input("Ingresa un año: "))

if año % 4 == 0 and año % 100 != 0:
    print(f"El año {año} es bisiesto. (Porque es divisible por 4 pero no por 100).")
elif año % 400 == 0:
    print(f"El año {año} es bisiesto. (Porque es divisible por 400).")
else:
    print(f"El año {año} no es bisiesto. (Porque no es divisible por 4).")

