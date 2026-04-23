# p134-cuadro-caracter.py
# Dados renglones, columnas, caracter y dibuja un cuadro

def dibuja_cuadro(renglones: int, columnas: int, caracter: str) -> None:
    for r in range(renglones):
        for c in range(columnas):

            print(caracter, end='')
print('') 

renglones = int(input('Ingrese el numero de renglones del cuadro: '))
columnas = int(input('Ingrese el numero de columnas del cuadro: '))
caracter = input('Ingrese el caracter para dibujar el cuadro: ')
dibuja_cuadro(renglones, columnas, caracter)