# p147-aleatorios.py
# Genera dos listas de números aleatorios y crea una tercera lista que sea la suma de las dos primeras

import random

from typing import List

def generar_aleatorios(n: int, min: int, max: int) -> List[int]:
    numeros_aleatorios = []
    for _ in range(n):
        numero = random.randint(min, max)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

def sumar_listas(lista1: List[int], lista2: List[int]) -> List[int]:
    suma = []
    for a, b in zip(lista1, lista2):
        suma.append(a + b)
    return suma

def main() -> None:
    MAX = 100
    lista1 : List[int] = generar_aleatorios(MAX, 1, 10)
    lista2 = generar_aleatorios(MAX, 20, 40)
    lista3 = sumar_listas(lista1, lista2)
    print(f"Lista 1: {lista1} - len{lista1}")
    print(f"Lista 2: {lista2} - len{lista2}")
    print(f"lista 3: {lista3} - len{lista3}")

if __name__ == "__main__":
    main()