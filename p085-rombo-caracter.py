# p085-rombo-caracter.py
# Dibuja un rombo con altura y ancho máximo impar

n = int(input("Dame un número impar para la altura: "))
caracter = input("¿Qué carácter quieres usar? ")

# Vali sea impar
if n % 2 == 0:
    print("El número debe ser impar.")
else:
    print()

    # Parte superior 
    for i in range(1, n + 1, 2):
        print(caracter * i)

    # Parte inferior 
    for i in range(n - 2, 0, -2):
        print(caracter * i)