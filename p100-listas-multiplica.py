# p100-listas-multiplica.py
# leer dos listas con 5 elementos numeros 
# crear 3er lista mult elementos de las dos lista 
# imprir 3 listas 

print('\033[H\033[J')
print("Multiplicación de elementos de dos listas\n")

# --- Captura de datos ---
lista_a = []
lista_b = []
lista_c = []

print("Introduzca 5 números para la Lista A:")
for i in range(5):
    while True:
        try:
            n = float(input(f"A[{i+1}]: "))
            lista_a.append(n)
            break
        except ValueError:
            print("Error: introduce un número válido.")

print("\nIntroduzca 5 números para la Lista B:")
for i in range(5):
    while True:
        try:
            n = float(input(f"B[{i+1}]: "))
            lista_b.append(n)
            break
        except ValueError:
            print("Error: introduce un número válido.")

# --- Procesamiento ---
for i in range(5):
    producto = lista_a[i] * lista_b[i]
    lista_c.append(producto)

# --- Resultados ---
print("\n--- Resultados ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C (A * B): {lista_c}")