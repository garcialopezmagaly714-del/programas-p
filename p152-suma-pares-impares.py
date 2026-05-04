# p152-suma-pares-impares.py
# Funcion que suma numeros pares o impares en un rango

def suma_rango(inicio: int, fin: int, tipo: str) -> int:
 
    suma = 0

    for n in range(inicio, fin + 1):
        if tipo == "P" and n % 2 == 0:
            suma += n
        elif tipo == "I" and n % 2 != 0:
            suma += n
    return suma

def main() -> None:
    print(" Suma en Rango ")
    inicio = int(input("Introduce el numero inicial: "))
    fin = int(input("Introduce el numero final: "))
    tipo = input("Que deseas sumar? (P)ares o (I)mpares: ").upper()

    if tipo not in ["P", "I"]:
        print("Error: opcion no valida.")
        return

    resultado = suma_rango(inicio, fin, tipo)

    if tipo == "P":
        print(f"La suma de los numeros pares entre {inicio} y {fin} es: {resultado}")
    else:
        print(f"La suma de los numeros impares entre {inicio} y {fin} es: {resultado}")

if __name__ == "__main__":
    main()
    