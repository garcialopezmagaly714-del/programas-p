#p020-numero-suerte.py
#Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos

# Solicitar el año de nacimiento
anio = input("Ingresa tu año de nacimiento: ")

print("Dígitos individuales:")
for digito in anio:
    print(digito)

suma = 0
for digito in anio:
    suma += int(digito)

print("La suma de los dígitos es:", suma)