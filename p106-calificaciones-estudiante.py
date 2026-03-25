# p106-calificaciones-estudiante.py
# Gestión de calificaciones de un estudiante usando diccionarios
print('\033[H\033[J')
print('Gestión de calificaciones de un estudiante usando diccionarios')
materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
califs = [10, 9, 8, 7.5, 6]
print(f'Lista de materias : \n{materias}\n')
print(f'Lista de calficaciones: \n{califs}\n')
notas = dict(zip(materias, califs))
print(f'\nDiccionario nuevo juntando las listas: \n {len(notas)} - {notas} ')
notas.update({'Ingles':10})
notas.update({'Programacion':7})
print(f'\nSe agregaron elementos) : \n{len(notas)} - {notas}')
notas.pop('Fisica')
notas.popitem()
print(f'\nSe removieron elementos : \n {len(notas)} - {notas}')
notas.update({'Quimica':10})
notas.update({'Matematicas':10})
print(f'\nSe modificaron elementos : \n{notas}')
s = 0

print('\nMaterias y calificaciones finales')
for m, c in notas.items():
 print(f'{m:<12} - {c:5}')
 s += c

p = s / len(notas)
print(f'\nLa suma: {s} y el promedio: {p:.2f}')

notas.clear()
print(f'\nSe borró todo : {notas}')