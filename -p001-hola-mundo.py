#-p001-hola-mundo.py
#lee datos y envia un saludo

print('leyendo datos y enviando un saludo:\n')

nombre = input('Dame tu nombre ?')
Edad = int(input ('Dame tu edad?'))
Peso = float (input('Dame tu peso?'))

print(f'{nombre} bienvendido a pyyhon, tu edad es {Edad}, tu peso es {Peso}')
print(type(nombre))
print(type(Edad))
print(type(Peso))
