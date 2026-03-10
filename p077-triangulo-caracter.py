# p077-triangulo-caracter.py
# Imprime un triángulo rectángulo de caracteres

print('\033[H\033[J')

n = int(input("¿Cuántos renglones tendrá el triángulo? "))
car = input("¿Qué carácter quieres usar para dibujar? ")

print("\n--- Triángulo Generado ---")

# Bucle exterior: controla las filas
for i in range(1, n + 1):
    # Bucle interior: controla las columnas (o caracteres por fila)
    # El rango llega hasta 'i' para que cada fila tenga 'i' caracteres
    for j in range(i):
    # 'end=""' evita el salto de línea para imprimir en la misma fila
            print(car, end="")
# 'print()' genera el salto de línea para pasar a la siguiente fila
print()