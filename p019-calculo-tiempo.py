#p019-calculo-tiempo.py
#Diseña un programa que tome una cantidad de horas como un número entero

horas = int(input("Ingresa la cantidad de horas: "))

dias = horas / 24
minutos = horas * 60
segundos = horas * 60 * 60

print("Equivalencia del tiempo ingresado:")
print("Días:", dias)
print("Minutos:", minutos)
print("Segundos:", segundos)