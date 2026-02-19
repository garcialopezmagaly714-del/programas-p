# p046-conteo-descendente.py
# Imprime los números de 100 a 1 usando un ciclo while
print('\033[H\033[J')
print("Numeros de 1-100 con while ")


r = 100

while r >= 1:
    print(r)
    r = r - 1

print(f'\nciclo termminado: {r}')