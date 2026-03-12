# p083-plan-ahorro-depistos-mensuales.py

#  plan de ahorro con depósitos mensuales e interés compuesto mensual

monto_inicial = float(input("Monto inicial de ahorro: "))
deposito = float(input("Depósito mensual: "))
tasa = float(input("Tasa de interés mensual (%): "))
meses = int(input("Número de meses a simular: "))

print("--- Plan de Ahorro Detallado ---")

saldo = monto_inicial

mes = 1
while mes <= meses:
    saldo_inicial = saldo
    interes = saldo_inicial * (tasa / 100.0)
    saldo = saldo_inicial + interes + deposito
    print(f"Mes {mes}: Saldo Inicial: ${saldo_inicial:.2f} | Interés: ${interes:.2f} | Saldo Final: ${saldo:.2f}")
    mes = mes + 1

print(f"Al final de {meses} meses, tendrás ${saldo:.2f}")