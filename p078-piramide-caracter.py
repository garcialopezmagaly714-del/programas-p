# p078-piramide-caracter.py
# Imprime una piramide de caracteres

print('\033[H\033[J')
print('Imprime una piramide de caracteres')

altura = int(input("Introduce la altura de la pirámide: "))
car = input("Introduce el carácter para la pirámide: ")

print("\n--- Pirámide Generada ---")

# Bucle exterior para cada nivel de la pirámide
for i in range(1, altura + 1):

    # Calcular espacios y caracteres para el nivel actual
    espacios = altura - i
    caracteres = 2 * i - 1

    # Primer bucle interior: Imprimir los espacios en blanco a la izquierda
    for j in range(espacios):
        print(" ", end="")
# Segundo bucle interior: Imprimir los caracteres
for k in range(caracteres):
    print(car, end="")

# Salto de línea para pasar al siguiente nivel
print()