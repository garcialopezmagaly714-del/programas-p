#p004-paga-trabajador.py


print('Calculando la paga de un trabajador')

nombre = input('nombre > ')
horas = int(input('Horas trabajadas > '))
paga = float(input('Paga x hora > '))

tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
# salida
print('Resumen de pagos : \n')
print(f'El trabajador {nombre}, trabajo{horas} horas, con una paga de {paga} pesos, impuestos de {tasa} %')
print(f'paga bruta : {pagabruta}')
print(f'Impuesto : {impuesto}')
print(f'Paga Neta : {paganeta}')
