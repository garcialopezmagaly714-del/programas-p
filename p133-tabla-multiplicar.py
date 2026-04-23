#p133-tabla-multiplicar.py
# Dada una tabla y un limite de la tabla, imprime la tabla hasta el limite 

def tabla_multiplicar(tabla:int,limite:int)->None:
    print(f'Tabla de multiplicar del {tabla} hasta el {limite}: ')
    for i in range (1,limite +1):
     resultado = tabla
     print(f'{tabla} x {i} = {resultado}')
    print('') 

# Solicita al usuario la tabla y el limite 
tabla= int (input('Ingrese la tabla de multiplicar que dese (ej.5)'))
limite = int (input('Ingrese el limite hasta donde desea multiplicar(ej.10):'))
tabla_multiplicar(tabla,limite)

# ejemplo de uso
tabla_multiplicar(5,10)