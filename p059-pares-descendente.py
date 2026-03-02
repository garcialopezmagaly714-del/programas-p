# p059-pares-descendente.py
# Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.


while True:
    print("\n Impresión de números pares descendente ")
    
    # Solicitar el número n al usuario
    n = int(input("Introduce un número límite (menor a 100): "))
    
    # El contador inicia en 100
    i = 100  

    # Acumulador para la suma total      
    suma = 0       
    
    print("Números pares: ", end="")
    
    # El ciclo continúa mientras i sea mayor o igual al número n
    while i >= n:
        if i % 2 == 0:        # Verificamos si es par
            print(f"{i}", end=" ")
            suma += i
        i -= 1                
    
    print(f"\nLa suma de los pares es: {suma}")
    
    # Preguntar si desea continuar
    res = input("\n¿Desea continuar (S/N)? ").upper()
    if res == "N":
        print("\nSaliendo del programa...")
        break