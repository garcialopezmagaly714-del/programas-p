# p120-contar-caracteres.py
# Contar la frecuencia de caracteres en una cadena de texto

print('\033[H\033[J')
print('Contar caracteres en una cadena de texto\n')

cadena = input('Ingrese una cadena: ')

# diccionario vacio
frecuencia = {}

for caracter in cadena:
    if caracter not in frecuencia:
        frecuencia[caracter] = 1
    else:
        frecuencia[caracter] += 1

print('Resultado:')
print(frecuencia)