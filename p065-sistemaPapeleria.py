# p065-sistemaPapeleria.py
# p065-sistemaPapeleria.py
"""
"""


cantidad_c = 0; total_c = 0.0; org_c = 0.0
cantidad_o = 0; total_o = 0.0; org_o = 0.0
cantidad_d = 0; total_d = 0.0; org_d = 0.0
cantidad_p = 0; total_p = 0.0; org_p = 0.0

ventas = 0


print("---------------------------------")
print("Papelería la Malena, SA. de CV.")
print("Sistema de ventas de copias")
print("---------------------------------")


while True:
    ventas += 1
    print(f"\nVenta: {ventas}")

    
    tipo = input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 ? ").strip().upper()
    while tipo not in ("C", "O", "D", "P"):
        tipo = input(">>> Error. Tipo no válido. Ingrese C, O, D o P: ").strip().upper()

    # ENTRADA
    cant_str = input("Cantidad ? ").strip()
    while not cant_str.isdigit() or int(cant_str) <= 0:
        cant_str = input("Cantidad inválida. Ingrese un entero > 0: ").strip()
    cantidad = int(cant_str)

   
    if tipo == "C":
        precio = 3.0
    elif tipo == "O":
        precio = 4.0
    elif tipo == "D":
        precio = 6.0
    else:
        precio = 12.0

    subtotal_original = precio * cantidad
    subtotal_final = subtotal_original

    if cantidad > 50:
        subtotal_final = subtotal_original * 0.90
        print("*** Descuento del 10% aplicado por volumen! ***")

    
    if tipo == "C":
        cantidad_c += cantidad
        total_c += subtotal_final
        org_c += subtotal_original
    elif tipo == "O":
        cantidad_o += cantidad
        total_o += subtotal_final
        org_o += subtotal_original
    elif tipo == "D":
        cantidad_d += cantidad
        total_d += subtotal_final
        org_d += subtotal_original
    else:
        cantidad_p += cantidad
        total_p += subtotal_final
        org_p += subtotal_original

    # Otra venta
    otra = input("Otra venta (S/N) ? ").strip().upper()
    while otra not in ("S", "N"):
        otra = input("Responde S o N: ").strip().upper()
    if otra == "N":
        break


print("---------------------------------------")
print("Resumen diario de ventas")
print("---------------------------------------")
print("Ventas realizadas:", ventas)
print("-------------------------")

linea = f"Carta : {cantidad_c} - $ {total_c:0.2f}"
if round(org_c - total_c, 2) > 0: linea += f" (Precio original: $ {org_c:0.2f})"
print(linea)

linea = f"Oficio : {cantidad_o} - $ {total_o:0.2f}"
if round(org_o - total_o, 2) > 0: linea += f" (Precio original: $ {org_o:0.2f})"
print(linea)

linea = f"Doble Of. : {cantidad_d} - $ {total_d:0.2f}"
if round(org_d - total_d, 2) > 0: linea += f" (Precio original: $ {org_d:0.2f})"
print(linea)

linea = f"Plano : {cantidad_p} - $ {total_p:0.2f}"
if round(org_p - total_p, 2) > 0: linea += f" (Precio original: $ {org_p:0.2f})"
print(linea)

print("-------------------------")

total_copias = cantidad_c + cantidad_o + cantidad_d + cantidad_p
total_general = total_c + total_o + total_d + total_p
print("Tot. Ventas :", total_copias, "- $", f"{total_general:0.2f}")

if total_general < 50.0:
    mensaje = "Venta moderada"
elif total_general <= 150.0:
    mensaje = "Venta frecuente"
else:
    mensaje = "Venta superada"

print("Esta venta es una :", mensaje)


              