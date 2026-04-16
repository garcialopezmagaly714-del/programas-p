# p116-modificar-diccionario.py
# Modifica los valores en un diccionario

print('\033[H\033[J')
print('Modificar valores en un diccionario\n')

paises = {
    'Argentina': 100,
    'Brasil': 200,
    'Colombia': 300,
    'Chile': 400,
    'Ecuador': 500,
    'Bolivia': 600,
    'Jamaica': 700
}

print(f'Diccionario inicial:\n{paises} - {len(paises)}\n')

paises['Brasil'] = 250
paises['Chile'] = 450
paises.update({'Bolivia': 650})
paises.update({'Jamaica': 750})

print(f'Diccionario modificado:\n{paises} - {len(paises)}')