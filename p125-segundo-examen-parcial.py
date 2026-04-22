# p125-segundo-examen-parcial.py
# Alumna:Magaly Juanita Garcia Lopez
#Matricula: 20202188
# Proyecto: AeroRegistro

def ejecutar_examen():
    vuelos = [] # Lista principal para almacenar los diccionarios de vuelos

    print("--- AeroRegistro: Captura de Vuelos ---")

# Explicacion 1:Para capturar los datos este  Se usa un ciclo while que no se detiene hasta que presionas "Enter" sin escribir nada en el número de vuelo.  

    # SECCIÓN 1: CAPTURA DE DATOS
    while True:
        num = input("\nNo. Vuelo (vacío para terminar): ").strip()
        if not num: break # Detiene la captura si no hay texto [cite: 17]
        
        # Guardamos la entrada del usuario en un diccionario 
        vuelo = {
            'no': num,
            'orig': input("Origen: "),
            'dest': input("Destino: "),
            'aero': input("Aerolínea: "),
            'pax': int(input("Pasajeros: ")), # Convertir a entero para sumar [cite: 24]
            'precio': float(input("Tarifa: ")) # Convertir a decimal para promedios [cite: 25]
        }
        vuelos.append(vuelo)

    if not vuelos: return
#Explicaccion 2: Para Almacenar  Cada registro se guarda en un diccionario (para identificar datos por nombre) y luego se añade a una lista (para agrupar todos los vuelos).
    # SECCIÓN 2: DATOS CRUDOS Y TABLA
    print("\nDatos Crudos:", vuelos) # Requisito: Imprimir lista tal cual [cite: 18]
    
    print(f"\n{'No. Vuelo':<10} {'Destino':<15} {'Aerolínea':<15} {'Tarifa':<10}")
    print("-" * 50)
    for v in vuelos:
        # Formato tabular alineado a la izquierda (<) [cite: 19]
        print(f"{v['no']:<10} {v['dest']:<15} {v['aero']:<15} ${v['precio']:<10,.2f}")

#Explicacion 3: Es el procesamiento el programa recorre la lista una sola vez para sumar pasajeros, calcular el costo total y comparar quién es el más caro o barato.
    
    # SECCIÓN 3: CÁLCULOS Y RESUMEN [cite: 20]
    total_pax = sum(v['pax'] for v in vuelos)
    total_dinero = sum(v['precio'] for v in vuelos)
    v_caro = max(vuelos, key=lambda x: x['precio']) # Busca el vuelo con precio máximo [cite: 26]
    v_barato = min(vuelos, key=lambda x: x['precio']) # Busca el vuelo con precio mínimo [cite: 26]

    # Conteos por Aerolínea y Destino 
    aereos = {}
    destinos = {}
    for v in vuelos:
        aereos[v['aero']] = aereos.get(v['aero'], 0) + 1
        destinos[v['dest']] = destinos.get(v['dest'], 0) + 1

# Explicacion 4: se empieza el conteo Se usan diccionarios pequeños para contar cuántas veces se repite cada aerolínea y cada destino de forma automática.
    # SALIDA FINAL DE RESULTADOS
    print(f"\nRESUMEN FINAL:")
    print(f"Vuelos totales: {len(vuelos)}") # [cite: 21]
    print(f"Pasajeros -> Total: {total_pax}, Promedio: {total_pax/len(vuelos):.2f}") # [cite: 24]
    print(f"Tarifas -> Total: ${total_dinero:,.2f}, Promedio: ${total_dinero/len(vuelos):.2f}") # [cite: 25]
    print(f"Más caro: {v_caro['no']} (${v_caro['precio']:,.2f})") # [cite: 26]
    print(f"Más barato: {v_barato['no']} (${v_barato['precio']:,.2f})") # [cite: 26]

    print("\nVuelos por Aerolínea:", aereos)
    print("Vuelos por Destino:", destinos)

if __name__ == "__main__":
    ejecutar_examen()