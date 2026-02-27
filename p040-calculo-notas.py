
# p040-calculo-notas.py
# Calcular el promedio de 5 calificaciones ingresadas por el usuario.

print("Ingresa 5 calificaciones (de 5 a 10):")

cal1 = float(input("Calificación 1: "))
cal2 = float(input("Calificación 2: "))
cal3 = float(input("Calificación 3: "))
cal4 = float(input("Calificación 4: "))
cal5 = float(input("Calificación 5: "))

promedio = (cal1 + cal2 + cal3 + cal4 + cal5) / 5

print(f"\nEl promedio es: {promedio:.2f}")

if promedio <= 6:
    print("Quedas reprobado")
elif promedio <= 7:
    print("Pasas de panzazo")
elif promedio <= 8:
    print("Muy bien, puedes mejorar")
elif promedio <= 9:
    print("Excelente, sigue así")
elif promedio <= 10:
    print("Perfecto, tu esfuerzo valió la pena")
else:
    print("Error: promedio fuera de rango")
    
print("\nPrograma terminado")

#-p040-calculo-notas.py
#-programa que calcule el promedio de 5 calificaciones ingresadas por el usuario
# Menor a 6: "Quedas reprobado"
# Desde 6 hasta menos de 7: "Pasas de panzazo"
# Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
# Desde 8 hasta menos de 9: "Excelente, sigue así"
# Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena"

import os; os.system("cls")

print("Calcula el promedio de 5 calificaciones e imprime resultado")

print("Introduce las cinco calificaciones, separadas por un enter")
n1,n2,n3,n4,n5 = float(input()), float(input()), float(input()), float(input()), float(input())

p = (n1 + n2 + n3 + n4 + n5) / 5

if p >= 0 and p < 6:
    print(f"El promedio es {p}, Quedas reprodado")
if p >= 6 and p < 7:
    print(f"El promedio es {p}, Pasas de panzazo")
if p >= 7 and p < 8:
    print(f"El promedio es {p}, Muy bien pues mejorar")
if p >= 8 and p < 9:
    print(f"El promedio es {p}, Excelente sigue asi")
if p >= 9 and p <= 10:
    print(f"El promedio es {p}, Perfecto tu esfuerzo valio la pena")

print("\nProceso terminado ... ")

