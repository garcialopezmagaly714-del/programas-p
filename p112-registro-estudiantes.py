# p112-registro-estudiantes.py
# Crea una lista de diccionarios para representar un registro de estudiantes

grupo = [
    {'nombre':'Carlos','edad':45,'carrera':'sistemas','promedio':9} ,
    {'nombre':'Rocio','edad':35,'carrera':'sistemas','promedio':10}
]

print('\033[H\033[J')
print('Registro de Estudiantes\n')

print(f'\nGrupo inicial:{grupo} - {len(grupo)}')

print('\nCaptura de nuevos estudiantes')
while True:
    print(f'Datos Estudiante:')
    datos = {}
    nombre = input('Nombre ? ')
    if nombre =='': break
    datos['nombre'] = nombre
    datos['edad'] = int(input('Edad? '))
    datos['carrera'] = input('Carrera ? ')
    datos['promedio'] = float(input('Promedio? '))
    grupo.append(datos)

print(f'\nGrupo de estudiantes: {grupo} - {len(grupo)}')


print('\nDatos en forma de Tabla:')
print('-'*60)
for k in grupo[0].keys():
    print(f'{k:<13}', end='')
print()
print('-'*60)
for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<13}', end='')
    print()
print('-'*60)

print('\nDatos en forma de Registro y Cálculo de Promedios:')
print('-'*60)
suma = 0
for alumno in grupo:
    suma = suma + alumno['promedio']
    for k,v in alumno.items():
        print(f'{k:<12} : {v:>12}')
    print()
print('_'*50)

print('Suma : ', suma)
print('Promedio : suma / len{grupo}')