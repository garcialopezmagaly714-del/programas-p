#-p038-dia-semana.py
# Función que pida un número entero entre 1 y 7 y devuelva el día de la semana con letra.

import os

def dia(n):
    if n == 1:
        return "Domingo"
    elif n == 2:
        return "Lunes"
    elif n == 3:
        return "Martes"
    elif n == 4:
        return "Miércoles"
    elif n == 5:
        return "Jueves"
    elif n == 6:
        return "Viernes"
    elif n == 7:
        return "Sábado"
    else:
        return "Error: Día inválido."
    
# Principal
os.system("cls")
n = int(input("Dame un número (1-7) y te daré el día de la semana: "))
print(f"El día es {dia(n)}")
