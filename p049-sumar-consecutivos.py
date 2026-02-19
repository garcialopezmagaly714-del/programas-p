# p049-sumar-consecutivos.py
# Suma números hasta un total de 5000, pero cuenta hasta el 200

print('\033[H\033[J')
print('cuantos boletos tengo que vender para juntar 5000')

n= int(input('cuantos quieres recaudar?'))
b= 0
d = 0


while b < 200:
    b = b + 1
    d = d + b
    print(b, end= '')

    if d >= 5000:
        print("ya tengo el dinero que propuse")
        break

print(f"Use {b} boletos para llegar a  ${d}.")