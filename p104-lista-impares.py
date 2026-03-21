# p104-lista-impares.py
# Programa para realizar una lista de numeros impares y buscar elementos


n = int(input("Introduzca la cantidad de numeros impares (n): "))

print("\n--- Generacion de Lista ---")

impares = []

for i in range(n):
    impares.append(2 * i + 1)

print(f"Lista de los primeros {n} numeros impares:", impares)
print("\n--- Calculos ---")

suma = 0
for num in impares:
    suma += num

promedio = suma / len(impares)

print("Suma de los numeros:", suma)
print("Promedio de los numeros:", promedio)
print("\n--- Divisibles entre 3 ---")

div3 = []
for num in impares:
    if num % 3 == 0:
        div3.append(num)

suma_div3 = 0
for num in div3:
    suma_div3 += num

print("Numeros divisibles entre 3:", div3)
print("Suma de los numeros divisibles entre 3:", suma_div3)

print("\n--- Busqueda ---")

buscar = int(input("Introduzca elemento a buscar: "))
if buscar in impares:
    indice = impares.index(buscar)
    print(f"Resultado: El elemento {buscar} esta en la lista en la posicion (indice) {indice}.")
else:
    print(f"Resultado: El elemento {buscar} no esta en la lista.")

print("\nPrograma terminado")