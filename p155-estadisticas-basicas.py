# p155-estadisticas-basicas.py
# Calcula estadisticas basicas de una lista de numeros

def leer_lista() -> list[int]:
    entrada = input("Dame numeros (separados por espacio): ")
    partes = entrada.split()
    numeros = []
    for p in partes:
        numeros.append(int(p))
    return numeros

def mayor(lista: list[int]) -> int:
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista: list[int]) -> int:
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def media(lista: list[int]) -> float:
    suma = 0
    for n in lista:
        suma += n
    return suma / len(lista)

def varianza(lista: list[int]) -> float:
    prom = media(lista)
    suma = 0
    for n in lista:
        suma += (n - prom) ** 2
    return suma / len(lista) 

def desviacion(lista: list[int]) -> float:
    return varianza(lista) ** 0.5

def main() -> None:
    numeros = leer_lista()

    print(f"Lista de numeros: {numeros}")
    print(f"Media : {media(numeros)}")
    print(f"Mayor : {mayor(numeros)}")
    print(f"Menor : {menor(numeros)}")
    print(f"Varianza : {varianza(numeros)}")
    print(f"Desviacion estandar: {desviacion(numeros)}")

if __name__ == "__main__":
    main()