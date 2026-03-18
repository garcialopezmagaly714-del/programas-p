# p096-registro-estudiantes.py
# Registro y analisis de asistentes a un evento

print('\033[H\033[J') 
print('Sistema de registro para evento\n')
print("Introduce los nombres y edades de los asistentes (* en nombre para terminar)\n")


nombres = []
edades = []

# Ciclo para la captura de datos

while True:
    nombre = input("Nombre del asistente: ")
    if nombre == "*":
        break  # Termina el ciclo si el nombre es *
    try:
        edad = int(input(f"Edad de {nombre}: "))
        nombres.append(nombre)  # Agrega el nombre a la lista
        edades.append(edad)     # Agrega la edad en la misma posición
    except ValueError:
        print("Por favor, introduce una edad válida (número entero).")

# --- Generación de Reportes ---
if not nombres:
    print("\nNo se registraron asistentes.")
else:
    # 1. Reporte de asistentes mayores de edad
    print("\n--- Asistentes Mayores de Edad ---")
    encontrados = False
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(f"Nombre: {nombres[i]}, Edad: {edades[i]}")
            encontrados = True

    if not encontrados:
        print("No hay asistentes mayores de edad.")

    # 2. Reporte del asistente con mayor edad
    edad_maxima = max(edades)
    posicion_max = edades.index(edad_maxima)  # Encuentra la primera ocurrencia de la edad máxima
    nombre_max = nombres[posicion_max]
    print("\n--- Reconocimiento al Asistente de Mayor Edad ---")
    print(f"El asistente de mayor edad es: {nombre_max} con {edad_maxima} años.")