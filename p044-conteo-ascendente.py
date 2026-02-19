# p044-conteo-ascendente.py
# Imprime los números de 1 a 100 usando un ciclo while

print('\033[H\033[J')
print("Numeros de 1-100 con while ")

z = 1

while z <= 100:
    print(z, end=" ")
    z = z + 1

print(f' \nCiclo terminado: {z}' )