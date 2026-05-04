# p154-calcula-factoriales.py
# Calcula el factorial de cada nmero en una lista

def leer_lista() -> list[int]:
    entrada = input("Dame los numeros (separados por espacio): ")
    partes = entrada.split()
    numeros = []
    for p in partes:
        numeros.append(int(p))
    return numeros

def factorial(n: int) -> int:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def procesar_lista(lista: list[int]) -> list[int]:
    factoriales = []
    for n in lista:
        factoriales.append(factorial(n))
    return factoriales

def main() -> None:
    numeros = leer_lista()
    lista_factoriales = procesar_lista(numeros)

    print(f"La lista de numeros originales: {numeros}")
    print(f"La lista con los factoriales: {lista_factoriales}")

if __name__ == "__main__":
    main()