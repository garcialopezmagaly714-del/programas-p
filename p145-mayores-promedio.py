# p145-mayores-promedio.py
# Función para obtener los números mayores al promedio de una lista

from typing import List

def promedio_lista(lista:List[float]) -> float:
    suma = 0
    if not lista:
        return 0.0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def mayores_al_promedio(lista:List[float]) -> List[float]:
    prom = promedio_lista(lista)
    mayores = []
    for numero in lista:
        if numero > prom:
            mayores.append(numero)
    return mayores
    
def main() -> None:

    numeros : List[float] = [1.5, 2.3, 3.7, 4.0, 5.5]
    promedio = promedio_lista(numeros)
    resultado = mayores_al_promedio(numeros)
    print(f'El promedio es : {promedio}')
    print(f"Números mayores al promedio: {resultado} - {len(resultado)}")

if __name__ == "__main__":
    main()