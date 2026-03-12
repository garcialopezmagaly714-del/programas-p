# p087-acceder-lista.py
# Acceder a elementos de una lista 

n = [10,20,30,40,60,70,10,20,99]

print('\033[H\033[J')
print('Aceder a los elementos de una lista\n')

print('\nLongitud y contenido de las mediciones: ')
print(f'Cuantas mediciones son {len(n)}')
print('Todas las mediciones: {n} ')

print('\nPor indice positivo: ')
print(f'Primera y ultima: {n[0]},{n[8]}')

print('\nPor indice negativo: ')
print(f'Primera y ultima: {n[-9]},{n[-1]}')

print('\nPor rango: ')
print(f'De la 2 a la 6 (6 no incluida): {n[2:6]}')

print('\nPor saltos: ')
print(f'Las primeras 3 desde el principo: {n[:30]}')
print(f'las ultimas 3 desde el 6 hasta el final {n[6:]}')