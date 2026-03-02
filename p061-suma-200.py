# p061-suma-200.py
# Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos números se introdujeron y la suma final.


while True:
    print("\n Alcanzar la meta de 200 ")
    
    suma = 0
    contador = 0
    meta = 200
    
    # El ciclo sigue mientras la suma sea menor a 200
    while suma < meta:
        num = float(input(f"Suma actual: {suma}. Introduce un número: "))
        suma += num
        contador += 1
    
    print("-" * 25)
    print("Meta de 200 alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de números introducidos: {contador}")
    
    # Aquí usamos de nuevo .upper() para validar la salida
    res = input("\n¿Desea continuar (S/N)? ").upper()
    if res == "N":
        print("\nSaliendo... ¡Buen trabajo!")
        break