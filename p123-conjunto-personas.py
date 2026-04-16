# p123-conjunto-personas.py
# Operaciones con conjuntos de personas

print('\033[H\033[J')
print(' Gestión de Conjuntos de Personas\n')

l1 = ['Juan', 'Maria', 'Pedro', 'Jose', 'Rocio']
l2 = ['Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther']

A = set(l1)
B = set(l2)

print('Conjuntos Base')
print(f'A (Lista 1): {A}')
print(f'B (Lista 2): {B}')

print('\nOperaciones entre Conjuntos')
print(f'Union (A | B): {A | B}')
print(f'Interseccion (A & B): {A & B}')
print(f'Diferencia (A - B): {A - B}')
print(f'Diferencia Simetrica (A ^ B): {A ^ B}')

subconjunto= {'Pablo', 'Mateo'}
superconjunto = {'Reynaldo', 'Angelica'}

print(f'(Pablo, Mateo) es subconjunto de B? : {subconjunto <= B}')
print(f'A es superconjunto de (Reynaldo, Angelica)? : {A >= superconjunto}')
print(f'Pedro en A : {'Pedro' in A}')
print(f'No se encuentra Lilia en el conjunto B? : {'Lilia' not in B}')

print("\n Programa terminado")