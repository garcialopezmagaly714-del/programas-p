# p086-triangulo-invertido-numeros.py

# Imprime un triángulo numérico invertido de altura n

n = int(input("Dame un número: "))

print()
for fila in range(n, 0, -1):         # desde n hasta 1
    for col in range(1, fila + 1):   # imprime de 1 hasta 'fila'
        print(col, end=" ")
    print()  # salto de línea