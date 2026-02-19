# p048-multiplos-continue.py
# Imprime solo los múltiplos de 10 hasta 200.

print('\033[H\033[J')
print(" Buscando múltiplos de 10 entre 1 y 200...")


c = 0

print(" que multiplos quieres")
n= int (input('Que multiplos quieres?'))

while c < 200:
    c = c + 1
    if c % n != 0:
        continue
    print(f" {c}", end=" ")

