#p016-tercer-angulo.py 
#Escribe un programa que determine el tercer ángulo de un triángulo


angulo1 = float(input("ingresa el primer ángulo: "))
angulo2 = float(input("ingresa el segundo ángulo: "))

angulo3 = 180 - (angulo1 + angulo2)

print("El tercer ángulo del triángulo es:", angulo3)