# p142-suma-lista.py 
# Función para sumar los elementos de una lista de números

from typing import List
def suma_lista(lista:List[float]) -> int:
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros : List[float] = [1.5, 2.3, 3.7, 4.8]
resultado = suma_lista(numeros)
print(f'La suma de los numeros es {resultado}')