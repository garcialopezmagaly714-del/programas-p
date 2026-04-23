# p140-promedio-letra.py
# Recibe un promedio y regresa: una letra y un mensaje (tupla)

def calificacion_a_letra(promedio: float) -> tuple[str, str]:
    letra = ''
    nota = ''
    if 90 <= promedio <= 100:
        letra = 'A'; nota = 'Excelente'
    elif 80 <= promedio < 90:
        letra = 'B'; nota = 'Bien'
    elif 70 <= promedio < 80:
        letra = 'C'; nota = 'Suficiente'
    elif 60 <= promedio < 70:
        letra = 'D'; nota = 'Deficiente'
    elif 0 <= promedio < 60:
        letra = 'F'; nota = 'Reprobado'
    else:
        letra = ''; nota = 'Calificación invalida'
    
    return letra, nota

def main() -> None:
    promedio = float(input("Introduce el promedio (0-100): "))
    let, mensaje = calificacion_a_letra(promedio)
    if let:
        print(f"Calificación: {let} - {mensaje}")
    else:
        print(mensaje)
if __name__ == "__main__":
    main()