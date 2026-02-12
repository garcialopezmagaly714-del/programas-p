#p022-resistencia-equivalente-paralelo.py
#Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo


R1 = float(input("Ingresa el valor de la resistencia R1: "))
R2 = float(input("Ingresa el valor de la resistencia R2: "))
R3 = float(input("Ingresa el valor de la resistencia R3: "))
R4 = float(input("Ingresa el valor de la resistencia R4: "))


rt = 1 / ((1/R1) + (1/R2) + (1/R3) + (1/R4))


print("La resistencia total equivalente es:", rt)