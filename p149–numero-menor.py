# p149–numero-menor.py
# Funcion que solicita 3 numeros y devuelve el menor

def pedir_menor() -> int:
    n1 = int(input("Introduce el primer numero: "))
    n2 = int(input("Introduce el segundo numero: "))
    n3 = int(input("Introduce el tercer numero: "))
    menor = n1 
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

def main() -> None:
    resultado = pedir_menor()
    print(f"El numero menor es: {resultado}")

if __name__ == "__main__":
    main()