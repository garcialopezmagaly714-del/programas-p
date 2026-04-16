# p115-crear-acceder-diccionario.py
# Crea un diccionario para representar los dias de la semana

print('\033[H\033[J')
print('Accediendo a elementos de un diccionario\n')

dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miercoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sabado',
    7: 'Domingo'
}
 
print(f'Diccionario inicial: \n{dias} - {len(dias)}\n')

print('Accediendo a elementos:')
print(f'Llave 1 : {dias[1]}')
print(f'Llave 7 : {dias[7]}')
print(f'Llave 5 : {dias.get(5)}')
print(f'Llave 7 : {dias.get(7)}')

print(f'\nDiccionario final: \n{dias} - {len(dias)}\n')