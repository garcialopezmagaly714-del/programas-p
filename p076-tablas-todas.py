# p076-tablas-todas.py
# Imprime las tablas de multiplicar de 1 a n, hasta m

print('\033[H\033[J')

n = int(input("¿Hasta qué tabla de multiplicar deseas generar? "))
m = int(input("¿Hasta qué número deseas multiplicar cada tabla? "))

print("\n--- Generando Tablas de Multiplicar ---")

# Bucle exterior: itera a través de cada número de tabla (ej: 1, 2, 3...)
for i in range(1, n + 1):
    print(f"\n--- Tabla del {i} ---")
    # Bucle interior: itera a través de los multiplicadores (ej: 1, 2, ... 10)
    for j in range(1, m + 1):
        resultado = i * j
        # Se encontró un error en el código original: usaba i*i en lugar de i*j
        print(f"{i} x {j} = {resultado}")