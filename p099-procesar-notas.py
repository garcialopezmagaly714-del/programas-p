# p099-procesar-notas.py
# leer numero indeterminado de notas entre 0 y 100 
# validar que todas las notas introducidas esten dentro del rango [0,100]
# p099-notas-estadisticas.py
# Lee calificaciones entre 0 y 100 hasta que se ingrese 0, y muestra estadísticas.

print('\033[H\033[J')
print("Procesador de calificaciones\n")

notas = []
suma = 0.0

while True:
    try:
        nota = float(input("Introduzca nota (0 para detener): "))
        if nota == 0:
            break
        if 0 < nota <= 100:
            notas.append(nota)
            suma += nota
        else:
            print("Entrada inválida, debe ser un valor entre 0 y 100.")
    except ValueError:
        print("Error: debes introducir un número válido.")

#  Resultados 
if len(notas) == 0:
    print("\nNo se introdujeron notas válidas.")
else:
    promedio = suma / len(notas)
    max_nota = max(notas)
    min_nota = min(notas)

    # menores promedio
    menores_promedio = []
    for n in notas:
        if n < promedio:
            menores_promedio.append(n)

    print("\n--- Resultados ---")
    print(f"Total de notas introducidas: {len(notas)}")
    print(f"Lista de notas: {notas}")
    print(f"Suma de notas: {suma}")
    print(f"Promedio de notas: {promedio:.1f}")
    print(f"Nota máxima: {max_nota}")
    print(f"Nota mínima: {min_nota}")
    print(f"Notas menores al promedio ({promedio:.1f}): {len(menores_promedio)}")
    print(f"Lista de notas menores al promedio: {menores_promedio}")