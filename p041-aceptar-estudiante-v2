# p041-aceptar-estudiante-v2.py
# Escribe un programa que solicite el nombre, sexo (h/m), edad y tres calificaciones de un aspirante.

# Solicitar datos
nombre = input("Ingresa el nombre: ")
sexo = input("Ingresa el sexo (Hombre/Mujer): ").lower()
edad = int(input("Ingresa la edad: "))

cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

# Calcular promedio
promedio = (cal1 + cal2 + cal3) / 3

# Evaluar condiciones
if sexo != "m":
    print(f"Lo sentimos, {nombre}. La universidad solo acepta mujeres.")
elif edad <= 21:
    print(f"Lo sentimos, {nombre}. No cumples con la edad requerida (mayores de 21 años).")
elif promedio < 8 or promedio > 9.5:
    print(f"Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} no está dentro del rango requerido (8 a 9.5).")
else:
    print(f"¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {promedio:.2f} está dentro del rango permitido.")

print("\nPrograma terminado")