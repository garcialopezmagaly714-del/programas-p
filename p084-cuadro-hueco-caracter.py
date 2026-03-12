# p084-cuadro-hueco-caracter.py
# Dibuja un cuadrado hueco con un carácter dado

lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
caracter = input("¿Qué carácter quieres usar? ")

print("\n--- Cuadrado Hueco ---")

for fila in range(lado):
    for col in range(lado):
        if fila == 0 or fila == lado - 1 or col == 0 or col == lado - 1:
            print(caracter, end=" ")
        else:
            print(" ", end=" ")
    print()