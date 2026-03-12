# p089-agregar-lista.py
# Agregar elementos a una lista

print('\033[H\033[J')
print('Agregar elementos a una lista')

num = [80.3, 12.5, 60.2, 30.4]
print(f'Datos iniciales: {num}\n')

print(f'Agregar 90 y 100 al final:')
num.append(90)
num.append(100)
print(f'Resultado : {num}\n')

print(f'Insertar 80 en la posición 4:')
num.insert(4, 80)
print(f'Resultado : {num}\n')

print(f'Externder datos agregando [110, 120, 130] se agregan al final:')
otros = [110, 120, 130]
num.extend(otros)
print(f'Resultado : {num}\n')