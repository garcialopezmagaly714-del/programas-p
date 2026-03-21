# p101-mes-día-nombre.py
# Programa para leer mes del 1 al 12 muestra su nombre y la cantidad de dias que tiene

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num_mes = int(input('Introduzca un numero de mes (1-12): '))

if 1 <= num_mes <= 12:
    print('\n--- Resultados ---')
    print(f'Mes: {meses[num_mes - 1]}')
    print(f'Dias: {dias[num_mes - 1]}')
else:
    print('Error: el numero debe estar entre 1 y 12.')

print("\nPrograma terminado")