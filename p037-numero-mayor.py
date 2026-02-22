# p037-numero-mayor.py
# Determinar el numero mayor de tres numeros

print('Determina el numero mayor de una serie de tres numeros')
print('Dame 3 números enteros separados por espacio:')

n1, n2, n3 = input().split()

n1, n2, n3 = int(n1), int(n2), int(n3)

if((n1 > n2) and (n1 > n3)):
    print(f'El numero mayor es: {n1}')
elif((n2 > n1) and (n2 > n3)):
    print(f'El numero mayor es: {n2}')
else:
    print(f'El numero mayor es: {n3}')
    
print ("\nPrograma terminado")