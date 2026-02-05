#p005-Calculadora-imc.py
#Calcular el IMC de una persona 

print('Calculando el indice de masa corporal (IMC) : \n')

peso_Kg = float(input('Dame tu peso en Kilogramos: '))
altura_m = float(input('Dame tu altura en metros: '))

imc=peso_Kg / altura_m ** 2 # El ** es un operador arimetico que eleva un numero a una potencia 
print(f'Si tienes un peso de {peso_Kg} y una altura de {altura_m} tu IMC es {imc:.2f}')
