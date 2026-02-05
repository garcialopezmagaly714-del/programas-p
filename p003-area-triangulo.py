#p003-area-triangulo.py
#Calcular el area de un triangulo 

print('Calculando el area de un Triangulo \n')

print('Dame la base y la altura separados por Enter')
base, altura = float(input()), float(input())

area = (base * altura ) / 2

print(f'El triangulo de base {base:.2f} y altura {altura:.2f} tiene un area de {area:.2f}')
