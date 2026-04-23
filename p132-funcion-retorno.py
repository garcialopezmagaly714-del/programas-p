# p132-funcion-retorno.py

def suma (n1:float,n2:float)-> float:
    return n1+n2

print('\nSuma de dos numeros constantes:')
# se guarda el valor retornado por la funcion 
suma_resultados= suma(10,20)
print(f"La suma es {suma_resultados}")

print('\nDame dos numeros separados por enter:')
a,b = int (input()), int(input())
#se imprime directamente el valor retornado por la funcion 
print(f"La suma de los numeros es {suma(a,b)}")