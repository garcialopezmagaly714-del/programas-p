# p098-producto-punto.py
# Cálculo del producto punto de dos vectores

# Vectores representados como listas
vector_a = [1, 3, -5]
vector_b = [4, -2, -1]
producto_punto = 0

print('\033[H\033[J')
print("--- Cálculo del Producto Punto ---\n")
print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}\n")

# 1. Verificar que los vectores tengan la misma longitud
if len(vector_a) == len(vector_b):
    # 2. Multiplicar elementos y sumar los resultados
    for i in range(len(vector_a)):
        producto = vector_a[i] * vector_b[i]
        producto_punto += producto
    # 3. Mostrar el resultado
        print(f"El producto punto de los vectores es: {producto_punto}")
    # El cálculo sería: (1*4) + (3*-2) + (-5*-1) = 4 - 6 + 5 = 3

else:
    print("Error: Los vectores deben tener la misma longitud para calcular el producto punto.")