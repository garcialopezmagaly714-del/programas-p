#p006-Conversor-temperatura.py
#Convertir temperatura de grados Celsius a Farenheit

print('Convirtiendo grados Celsius a Farenheit: \n')

celcius = float(input('Ingresa la temperatura en grados Celcius: '))

farenheit = (celcius * 9 / 5) + 32

print(f'{celcius:.2f} grados celcius, equivalente a {farenheit:.2f} grados farenheut')
