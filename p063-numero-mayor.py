# p063-numero-mayor.py
# Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el número más grande de todos los introducidos.

# p063-numero-mayor.py

while True:
    print("\n Encontrar el número mayor de una serie ")
    
    # Inicializamos con un número muy pequeño o el primero de la serie
    mayor = -float('inf') 
    cuenta = 0
    
    print("Introduce números (0 para terminar):")
    
    while True:
        num = float(input("> "))
        
        if num == 0:
            break
        
        # Si el número actual es más grande que el que recordamos, lo actualizamos
        if num > mayor:
            mayor = num
            
        cuenta += 1
    
    print("-" * 25)
    
    if cuenta > 0:
        print(f"El número mayor fue: {mayor}")
    else:
        print("No se introdujeron números.")
        
    res = input("\n¿Desea continuar (S/N)? ").upper()
    if res == "N":
        break