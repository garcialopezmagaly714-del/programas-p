#p042-precio-entrada-cine.py
#Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del cliente.

edad = int(input("Ingresa tu edad: "))

# Determinar el precio según la edad
if edad < 5:
    print("Tu entrada es gratis.")
elif edad <= 12:
    print("El precio de tu entrada es de $5.")
elif edad <= 64:
    print("El precio de tu entrada es de $10.")
else:
    print("El precio de tu entrada es de $7.")

print("\nPrograma terminado")