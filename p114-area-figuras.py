# p114-area-figuras.py
# Crear una lista de diccionarios para representar figuras geometricas

import math

figuras = {
    "Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
    "Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
    "Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}

print('\033[H\033[J')
print('Area de Figuras Geometricas\n')

print("Figuras disponibles:")
for k,v in figuras.items():
    print(f'{k:<10} - Formula: {v["formula"]}')

while True:
    fig = input('\nElige una Figura: ').title()
    if fig in figuras: break
    print("Error: Figura no valida.")

area = 0

if fig == 'Circulo':
    r = int(input('Radio : '))
    area = eval(figuras[fig]['formula'].replace('r', str(r)))
    print(f'formula: {figuras[fig]['formula']}')
elif fig=='Triangulo':
    b = int(input('Base : '))
    a = int(input('Altura : '))
    area = eval(figuras[fig]['formula'].replace('b', str(b)).replace('a',str(a)))
    print(f'formula: {figuras[fig]['formula']}')
elif fig=='Rectangulo':
    l = int(input('Largo : '))
    a = int(input('Ancho : '))
    area = eval(figuras[fig]['formula'].replace('l', str(l)).replace('a',str(a)))
    print(f'formula: {figuras[fig]['formula']}')

print(f'\nEl area del {fig} es : {area:.4f}')