# p151–medidas-longitud.py
# Conversor de unidades de longitud

def pulgadas_a_centimetros(pulgadas: float) -> float:
    return pulgadas * 2.54

def metros_a_pies(metros: float) -> float:
    return metros * 3.281

def main() -> None:
    while True:
        print("\n Conversor de Unidades ")
        print("1. Pulgadas a Centimetros")
        print("2. Metros a Pies")
        print("3. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            cantidad = float(input("Introduce la cantidad en pulgadas: "))
            resultado = pulgadas_a_centimetros(cantidad)
            print(f"{cantidad} pulgadas equivalen a {resultado} centimetros.")

        elif opcion == "2":
            cantidad = float(input("Introduce la cantidad en metros: "))
            resultado = metros_a_pies(cantidad)
            print(f"{cantidad} metros equivalen a {resultado} pies.")

        elif opcion == "3":
            print("Saliendo")
            break

        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()