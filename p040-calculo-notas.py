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