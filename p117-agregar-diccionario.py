# p117-agregar-diccionario.py
# Agrega nuevos elementos a un diccionario

print('\033[H\033[J')
print('Agregar elementos a un diccionario\n')

ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}

print(f'Diccionario inicial:\n{ventas} - {len(ventas)}\n')

ventas['Rocio'] = 2500
ventas['Mateo'] = 1567
ventas.update({'Andrea': 9567})
ventas.update({'Miguel': 1234})

print(f'Diccionario actualizado:\n{ventas} - {len(ventas)}')