# p093-procesar-calificaciones.py
# Procesa calificaciones en una lista

print('\033[H\033[J')

print('Procesador de calificaciones de un curso\n')
print("Introduce calificaciones entre 0 y 10 (usa 99 para terminar):\n")

calificaciones = []
suma = 0.0

while True:
    try:
        n = float(input("Calificación > "))
        if n == 99:
            break
        if 0 <= n <= 10:
            calificaciones.append(n)
            suma += n
        else:
            print("Error: la calificación debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

if not calificaciones:
    print("No se ingresaron calificaciones.")
else:
    promedio = suma / len(calificaciones)
    mayores_promedio = []
    for cal in calificaciones:
        if cal > promedio:
            mayores_promedio.append(cal)

    print(f"\nSe capturaron {len(calificaciones)} calificaciones.")
    print(f"Las calificaciones son: {calificaciones}")
    print("\n--- Estadísticas del Curso ---")
    print(f"Suma total : {suma}")
    print(f"Promedio   : {promedio}")
    print(f"Calificaciones mayores al promedio: {len(mayores_promedio)} -> {mayores_promedio}")
    print(f"Calificación más alta: {max(calificaciones)}")
    print(f"Calificación más baja: {min(calificaciones)}")