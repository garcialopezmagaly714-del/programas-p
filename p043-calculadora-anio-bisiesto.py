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