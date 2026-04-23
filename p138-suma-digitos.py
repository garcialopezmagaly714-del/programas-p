# p138-suma-digitos.py
# Dado un numero entero sumar sus digitos individuales

def suma_digitos(numero: int) -> int:
    suma=0
    for n in str(numero):
        suma = suma + int(n)
        print(n)
    return suma

def main() -> None:
    print('\033[H\033[J')
    n = int(input("Introduce un numero entero: "))
    resultado = suma_digitos(n)
    print(f"La suma de los digitos de {n} es {resultado}")

if __name__ == "__main__":
    main()