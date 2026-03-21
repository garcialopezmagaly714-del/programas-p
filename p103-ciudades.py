# p103-ciudades.py
# Programa para leer nombres de ciudades y filtrar las que inician con consonante


ciudades = []

while True:
    ciudad = input('Introduzca nombre de ciudad ($ para detener): ')
    if ciudad == '$':
        break
    ciudades.append(ciudad)

print('\n--- Resultados ---')
print('Total de ciudades introducidas:', len(ciudades))
print('Lista original:', ciudades)

for i in range(len(ciudades) - 1):
    for j in range(len(ciudades) - i - 1):
        if ciudades[j].lower() < ciudades[j + 1].lower():
            ciudades[j], ciudades[j + 1] = ciudades[j + 1], ciudades[j]

print('\nLista ordenada descendente:', ciudades)

consonantes = []
for c in ciudades:
    if c[0].lower() in "bcdfghjklmnpqrstvwxyz":
        consonantes.append(c)

print('\nCiudades que inician con consonante:', len(consonantes))
print('Lista de ciudades con consonante inicial:', consonantes)

print("\nPrograma terminado")