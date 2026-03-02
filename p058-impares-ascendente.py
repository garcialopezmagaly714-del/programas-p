# p058-impares-ascendente.py
# Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.

while True:
    print("\n Impresión de números impares ")
    
    n = int(input("Introduce un número límite: "))
    
   # Contador que inicia en 1 
    i = 1 
    # Acumulador para la suma total         
    suma = 0       
    
    print("Números impares: ", end="")
    
    while i <= n:
        if i % 2 != 0:
            print(f"{i}", end=" ")
            suma += i
        i += 1
    
    print(f"\nLa suma de los impares es: {suma}")
    
    # Preguntar si desea continuar
    res = input("\n¿Desea continuar (S/N)? ").upper()
    if res == "N":
        print("\n¡Hasta luego!")
        break