# p139-factorial.py
# Dado un número entero calcular su factorial

def factorial(numero: int) -> int:
    if numero < 0:
        return -1 # Factorial no definido para números negativos
    resultado = 1
    for i in range(2, numero + 1):
        resultado = resultado * i
        return resultado
def main() -> None:
    print('\033[H\033[J')
    numero = int(input("Introduce un numero entero para calcular su factorial: "))
    resultado = factorial(numero)
    if resultado == -1:
        print("El factorial no esta definido para numeros negativos.")
    else:
        print(f"El factorial de {numero} es {resultado}")

if __name__ == "__main__":
    main()