# p082-compara-rendimiento-inversion.py
# Compara el crecimiento de dos fondos de inversión con interés compuesto anual

print("--- Fondo de Inversión A ---")
monto_a = float(input("Monto inicial: "))
tasa_a = float(input("Tasa de interés anual (%): "))

print("--- Fondo de Inversión B ---")
monto_b = float(input("Monto inicial: "))
tasa_b = float(input("Tasa de interés anual (%): "))

años = int(input("Años a proyectar: "))

print("--- Comparación de Rendimientos Anuales ---")
print("Año | Fondo A | Fondo B")
print("-------------------------------------------")

saldo_a = monto_a
saldo_b = monto_b

# ciclo anual
año = 1
while año <= años:
    saldo_a = saldo_a * (1 + tasa_a / 100.0)
    saldo_b = saldo_b * (1 + tasa_b / 100.0)
    print(f"{año} | $ {saldo_a:.2f} | $ {saldo_b:.2f}")
    año = año + 1

# comparación final
if saldo_a > saldo_b:
    print(f"Resultado final: El Fondo A (${saldo_a:.2f}) superó al Fondo B (${saldo_b:.2f}).")
elif saldo_b > saldo_a:
    print(f"Resultado final: El Fondo B (${saldo_b:.2f}) superó al Fondo A (${saldo_a:.2f}).")
else:
    print(f"Resultado final: Ambos fondos empataron con ${saldo_a:.2f}.")