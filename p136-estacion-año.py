# p136-estacion-año.py
# Dado un número regresar una cadena con el nombre de la estación del año

def estacion_ano(mes: int) -> str:
    est =''
    if mes in [12, 1, 2]:
        est  = "Invierno"
    elif mes in [3, 4, 5]:
        est = "Primavera"
    elif mes in [6, 7, 8]:
        est = "Verano"
    elif mes in [9, 10, 11]:
        est= "Otoño"
    else:
        est = "Mes inválido"
        
    return est

print('Dame un número de mes (1-12):')
mes = int(input())
print(f'La estación del año para el mes {mes} es: {estacion_ano(mes)}')