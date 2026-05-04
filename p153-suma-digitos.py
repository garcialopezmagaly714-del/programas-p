# p153-suma-digitos.py
# Procesa una lista de numeros y calcula la suma de sus digitos

def leer_lista() -> list[int]:
    entrada = input("Dame los numeros (separados por espacio): ")
    partes = entrada.split()
    numeros = []
    for p in partes:
        numeros.append(int(p))
    return numeros

def suma_digitos(n: int) -> int:
    suma = 0
    for d in str(n):
        suma += int(d)
    return suma

def procesar_lista(lista: list[int]) -> list[int]:
    resultado = []
    for n in lista:
        resultado.append(suma_digitos(n))
    return resultado

def main() -> None:
    numeros = leer_lista()
    lista_suma = procesar_lista(numeros)

    print(f"La lista de numeros original : {numeros}")
    print(f"La lista con las suma de digitos de los numeros: {lista_suma}")

if __name__ == "__main__":
    main()
    