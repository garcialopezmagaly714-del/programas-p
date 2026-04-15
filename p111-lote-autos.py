# p111-lote-autos.py
# Crear una lista de diccionarios para representar un lote de autos

autos = [
    { 'marca':'Ford', 'modelo':'Mustang', 'año': 1964 },
    { 'marca':'VW', 'modelo':'Jetta', 'año': 2015 }
]

print('\033[H\033[J')
print('Listado de Autos')

autos.append({ 'marca':'Ford', 'modelo':'Focus', 'año': 2000 })
print(f'\nAutos : {autos} - {len(autos)}')

print('\nCada auto dentro de los autos:')
print('-'*50)
for auto in autos:
    print(auto)

print (f'Datos de los autos en forma de tabla')
print('_'*50)
for k in autos[0].keys():
    print(f'{k}\t', end='')

print()
print('_'*50)

for auto in autos:
    for v in auto.values():
        print(f'{v}\t', end='')

print()
print('_'*50)

print('\nDatos en forma de Registro')
print('-'*50)
suma_años = 0
for auto in autos:
    suma_años = suma_años + auto['año']
    for k,v in auto.items(): 
        print(f'{k:<12} : {v}')
    print('')

print('_'*50)

print('Suma años: ', suma_años)