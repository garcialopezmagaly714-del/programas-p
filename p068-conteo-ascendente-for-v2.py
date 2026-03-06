# p068-conteo-ascendente-for-v2.py
# Imprime los números de 1 a n, en incrementos de m, usando un ciclo for

print(" Iniciando secuencia de conteo ascendente...")

n = int(input("Hasta donde ? "))
m = int(input("De cuanto en cuanto ? "))

for i in range(1, n+1, m):
    print(i, end=' ')