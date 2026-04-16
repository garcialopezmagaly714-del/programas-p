# p124-conjunt-numeros.py
# Operaciones entre conjuntos numericos

print('\033[H\033[J')
print('Gestión de Conjuntos Numéricos\n')

l1 = [50, 60, 70, 80, 90, 100, 200]
l2 = [60, 90, 100, 300, 400, 500]
l3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(l1)
B = set(l2)
C = set(l3)

print('Conjuntos Base')
print(f'Lista 1: {A}')
print(f'Lista 2: {B}')
print(f'Lista 3: {C}')

print('\nOperaciones entre Conjuntos')
print(f'Union (A | B): {A | B}')
print(f'Union (B | C): {B | C}')
print(f'Diferencia (A - C): {A - C}')
print(f'Diferencia Simetrica (B ^ C): {B ^ C}')
print(f'Interseccion (B & C): {B & C}')

print(f"A es subconjunto de B? : {A <= B}")
print(f"C es subconjunto de A? : {C <= A}")
print(f"100 en A? : {100 in A}")
print(f"60 en A, B y C? : {60 in A and 60 in B and 60 in C}")
print(f"No esta el numero 900 en C? : {900 not in C}")

print("\nPrograma terminado")