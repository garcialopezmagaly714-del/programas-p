# p102-listas-aleatorios-suma.py
# Programa para generar dos listas aleatorias y una con la suma solo si ambos numeros son impares

import random

lista_a = []
lista_b = []
lista_c = []

for i in range(10):
    lista_a.append(random.randint(1, 100))
    lista_b.append(random.randint(1, 100))
    
for i in range(10):
    if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0:
        lista_c.append(lista_a[i] + lista_b[i])
    else:
        lista_c.append(0)

print('--- Listas Generadas ---')
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')

print('\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---')
print(f'Lista C: {lista_c}')

print("\nPrograma terminado")