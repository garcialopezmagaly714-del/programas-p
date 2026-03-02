# p062-conversion-temperaturas.py
# El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.

while True:
    print("\n Tabla de Conversión: Celsius a Fahrenheit ")
    
    # Solicitar el rango al usuario
    temp_inicial = int(input("Introduce la temperatura inicial en °C: "))
    temp_final = int(input("Introduce la temperatura final en °C: "))
    
    print("-" * 25)
    
    celsius = temp_inicial
    
    # El ciclo se ejecuta desde la temperatura inicial hasta la final
    while celsius <= temp_final:
        # Aplicamos la fórmula matemática
        fahrenheit = (celsius * 9/5) + 32
        
        # Imprimimos el resultado con formato
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
        
        # Incrementamos de uno en uno
        celsius += 1
    
    # Preguntar si desea realizar otra tabla
    res = input("\n¿Desea continuar (S/N)? ").upper()
    if res == "N":
        print("\nSaliendo del programa")
        break