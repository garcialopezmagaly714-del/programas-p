# p047-conteo-descendente-v2.py
# Imprime los números de n a 1, en decrementos de m, usando un ciclo while

print('\033[H\033[J')
print("Numeros de 1-100 con while ")

n = int(input("Desde donde ? "))
m = int(input("De cuanto en cuanto ? "))

r = n

while r >= 1:
    print(r)
    r = r -m

print(f'\nciclo termminado: {r}')