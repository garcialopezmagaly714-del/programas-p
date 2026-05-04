# p150-dia-semana.py
# Funcion que recibe un numero del 1 al 7 y devuelve el dia de la semana

def dia_semana(num: int) -> str:
    dias = [
        "Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes",
        "Sabado",
        "Domingo"
    ]

    if 1 <= num <= 7:
        return dias[num - 1]
    else:
        return "Error"

def main() -> None:
    numero = int(input("Introduce un numero del 1 al 7: "))
    resultado = dia_semana(numero)
    if resultado == "Error":
        print("Error: El numero debe estar entre 1 y 7.")
    else:
        print(f"El dia es: {resultado}")

if __name__ == "__main__":
    main()