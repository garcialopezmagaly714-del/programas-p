# p118-eliminar-diccionario.py
# Eliminar elementos de un diccionario

print('\033[H\033[J')
print('Eliminar elementos de un diccionario\n')

municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalpa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}

print(f'Diccionario inicial:\n{municipios} - {len(municipios)}\n')

del municipios['Apozol']
print(f'Despues de eliminar Apozol:\n{municipios} - {len(municipios)}\n')

municipios.pop('Fresnillo')
print(f'Despues de eliminar Fresnillo:\n{municipios} - {len(municipios)}\n')

municipios.popitem()
print(f'Despues de eliminar el ultimo elemento :\n{municipios} - {len(municipios)}\n')

municipios.clear()
print(f'Diccionario final: \n{municipios} - {len(municipios)}')