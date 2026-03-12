# p092-lista-de-gastos.py

# Gestiona una lista de gastos mensuales con menú y manejo de errores

# p087-gestiona-gastos.py
# Gestiona una lista de gastos mensuales con menú y manejo de errores

gastos = []  # lista donde guardaremos los montos (floats)

while True:
    print("\n=== GESTIÓN DE GASTOS MENSUALES ===")
    print("1) Ver gastos")
    print("2) Agregar gasto")
    print("3) Modificar gasto (por índice)")
    print("4) Eliminar gasto (por índice)")
    print("5) Ver TOTAL")
    print("6) Salir")

    opcion = input("Elige una opción (1-6): ").strip()

    if opcion == "1":
        # Ver gastos
        if len(gastos) == 0:
            print("No hay gastos registrados.")
        else:
            print("\n-- Lista de gastos --")
            for i, monto in enumerate(gastos, start=1):  # índices 1-based para el usuario
                print(f"{i}. ${monto:.2f}")

    elif opcion == "2":
        # Agregar gasto
        try:
            monto = float(input("Monto del gasto a agregar: ").strip())
            if monto < 0:
                print("⚠ El gasto no puede ser negativo.")
            else:
                gastos.append(monto)
                print(f"✔ Gasto agregado: ${monto:.2f}")
        except ValueError:
            print(" Entrada inválida. Debes escribir un número.")

    elif opcion == "3":
        # Modificar gasto por índice
        if len(gastos) == 0:
            print("No hay gastos para modificar.")
        else:
            try:
                idx = int(input(f"Índice a modificar (1 - {len(gastos)}): ").strip())
                if 1 <= idx <= len(gastos):
                    try:
                        nuevo = float(input("Nuevo monto: ").strip())
                        if nuevo < 0:
                            print("⚠ El gasto no puede ser negativo.")
                        else:
                            anterior = gastos[idx - 1]
                            gastos[idx - 1] = nuevo
                            print(f"✔ Gasto #{idx} actualizado de ${anterior:.2f} a ${nuevo:.2f}")
                    except ValueError:
                        print(" Entrada inválida. Debes escribir un número.")
                else:
                    print(" Índice fuera de rango.")
            except ValueError:
                print(" Entrada inválida. Debes escribir un número entero para el índice.")

    elif opcion == "4":
        # Eliminar gasto por índice
        if len(gastos) == 0:
            print("No hay gastos para eliminar.")
        else:
            try:
                idx = int(input(f"Índice a eliminar (1 - {len(gastos)}): ").strip())
                if 1 <= idx <= len(gastos):
                    eliminado = gastos.pop(idx - 1)
                    print(f"Gasto #{idx} eliminado (${eliminado:.2f}).")
                else:
                    print(" Índice fuera de rango.")
            except ValueError:
                print(" Entrada inválida. Debes escribir un número entero para el índice.")

    elif opcion == "5":
        # Ver total
        total = 0.0
        for m in gastos:
            total += m
        print(f"TOTAL de gastos: ${total:.2f}")

    elif opcion == "6":
        print("Saliendo... ¡Hasta luego!")
        break

    else:
        print(" Opción no válida. Elige del 1 al 6.")