# p088-modificar-lista.py
# Modificar los elementos de una lista

print('\033[H\033[J')
print('Modificar los elementos de una lista')

cal = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print(f'\nTodas las calificaciones: {cal}')

print(f'\nModificar calificaciones en posiciones [0] y [1] con 7 y 7:')
cal[0]=7
cal[1]=7
print(f'Resultado: {cal}')

print(f'\nModificar calificaciones en el rango [2:5] (5 no incluida) con 9,9,9:')
cal[2:5] = [9,9,9]
print(f'Resultado: {cal}')