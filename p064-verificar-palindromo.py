# p064-verificar-palindromo.py
# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).


while True:
    print("\n Verificar si un número es Palíndromo ")
    
    # Leemos el número como cadena para facilitar la comparación
    numero_str = input("Introduce un número para verificar si es palíndromo: ")
    
    # Usamos "slicing" de Python para invertir la cadena fácilmente
    # El formato [::-1] crea una copia de la cadena al revés
    numero_invertido = numero_str[::-1]
    
    if numero_str == numero_invertido:
        print(f"El número {numero_str} es un palíndromo.")
    else:
        print(f"El número {numero_str} no es un palíndromo.")
    
    # Preguntar si desea continuar
    res = input("\n¿Desea continuar (S/N)? ").upper()
    if res == "N":
        print("\nSaliendo del programa")
        break