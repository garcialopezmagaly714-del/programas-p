# p060-promedio-suma.py
# Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la suma y el promedio de la serie.


while True:
    print("\n Calcular suma y promedio de una serie ")
    
    suma = 0
    cuenta = 0
    
    print("Introduce números (0 para terminar):")
    
    while True:
        num = float(input("> "))
        
        if num == 0:
            break  # Sale del ciclo de lectura si el usuario ingresa 0
            
        suma += num
        cuenta += 1
    
    # Cálculos y resultados
    if cuenta > 0:
        promedio = suma / cuenta
        print("-" * 25)
        print(f"Se introdujeron {cuenta} números.")
        print(f"La suma es: {suma}")
        print(f"El promedio es: {promedio}")
    else:
        print("\nNo se introdujeron números válidos.")
    
    # Preguntar si desea continuar con otra serie
    res = input("\n¿Desea continuar (S/N)? ").upper()
    if res == "N":
        print("\nSaliendo del programa...")
        break