# -p066_primerExamenParcial.py

"""
Objetivo: Simular el sistema de venta de boletos de una función de cine (Clasificación 13+),
          registrando asistentes por tipo y sexo, rechazando menores de 13 años,
          y generando un reporte final con estadísticas e ingresos.
Nombre del Alumno: Magaly Juanita Garcia Lopez
Matrícula: 20202188
Materia: Computación Aplicada
Examen: Primer Parcial
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
total_estudiantes = 0
total_adultos = 0
total_tercera_edad = 0
total_academicos = 0

total_hombres = 0
total_mujeres = 0

total_asistentes = 0
total_rechazados = 0
suma_edades = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
ingresos_adultos = 0.0
ingresos_tercera_edad = 0.0
ingresos_academicos = 0.0
ingresos_totales = 0.0

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCERA_EDAD = 60.0
PRECIO_ACADEMICO = 70.0

print('\033[2J\033[H')
print(" --- Sistema de Venta de Boletos de Cine --- ")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":
    print("\n--- Nueva Venta ---")
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo de comprador y el sexo.
    # ¡Recuerda convertir la edad a un número entero!
    while True:
        try:
            edad = int(input("Introduce la edad del comprador: ").strip())
            if edad < 0:
                print("Edad no válida. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")

    # Menú de tipo de comprador: 1=Estudiante, 2=Adulto, 3=Tercera Edad, 4=Académico
    print("Tipo de comprador: [1=Estudiante, 2=Adulto, 3=Tercera Edad, 4=Académico]")
    tipo_op = input("Selecciona 1/2/3/4: ").strip()

    while tipo_op not in ("1", "2", "3", "4"):
        print("Opción no válida.")
        tipo_op = input("Selecciona 1/2/3/4: ").strip()

    sexo = input("Sexo (H/M): ").strip().upper()
    while sexo not in ("H", "M"):
        print("Opción no válida.")
        sexo = input("Sexo (H/M): ").strip().upper()

    # --- 2. Validación de Edad (Clasificación 13+) ---
    # La película es para 13 años o más.
    if edad >= 13:
        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        tipo_nombre = ""
        precio_boleto = 0.0

        if tipo_op == "1":
            tipo_nombre = "Estudiante"
            precio_boleto = PRECIO_ESTUDIANTE
            total_estudiantes += 1
            ingresos_estudiantes += PRECIO_ESTUDIANTE
        elif tipo_op == "2":
            tipo_nombre = "Adulto"
            precio_boleto = PRECIO_ADULTO
            total_adultos += 1
            ingresos_adultos += PRECIO_ADULTO
        elif tipo_op == "3":
            tipo_nombre = "Tercera Edad"
            precio_boleto = PRECIO_TERCERA_EDAD
            total_tercera_edad += 1
            ingresos_tercera_edad += PRECIO_TERCERA_EDAD
        else:  # "4"
            tipo_nombre = "Académico"
            precio_boleto = PRECIO_ACADEMICO
            total_academicos += 1
            ingresos_academicos += PRECIO_ACADEMICO

        sexo_txt = "Hombre" if sexo == "H" else "Mujer"
        print(f"¡Bienvenido(a)! Venta registrada: Edad {edad}, Sexo {sexo_txt}, Tipo {tipo_nombre}.")

        # --- 3. Actualización de Estadísticas Generales ---
        total_asistentes += 1
        suma_edades += edad
        if sexo == "H":
            total_hombres += 1
        else:
            total_mujeres += 1

        # --- 4. Actualización de Ingresos ---
        ingresos_totales += precio_boleto

    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        total_rechazados += 1

    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()
    while continuar_venta not in ("s", "n"):
        continuar_venta = input("Responde 'S' o 'N': ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
promedio_edad = 0
if total_asistentes > 0:
    promedio_edad = suma_edades / total_asistentes

# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
print(f"Total de Estudiantes: {total_estudiantes}")
print(f"Total de Adultos: {total_adultos}")
print(f"Total de Tercera Edad: {total_tercera_edad}")
print(f"Total de Académicos: {total_academicos}")
print("-------------------------------")
print(f"Total de Hombres: {total_hombres}")
print(f"Total de Mujeres: {total_mujeres}")
print("-------------------------------")
print(f"Total de Asistentes: {total_asistentes}")
print(f"Promedio de edad de asistentes: {promedio_edad:.2f} años")
print(f"Personas rechazadas por edad: {total_rechazados}")

print("\n--- Reporte de Ingresos ---")
print(f"Ingresos por Estudiantes: ${ingresos_estudiantes:,.2f}")
print(f"Ingresos por Adultos: ${ingresos_adultos:,.2f}")
print(f"Ingresos por Tercera Edad: ${ingresos_tercera_edad:,.2f}")
print(f"Ingresos por Académicos: ${ingresos_academicos:,.2f}")
print("-------------------------------")
print(f"TOTAL RECAUDADO: ${ingresos_totales:,.2f}")

print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
# Umbrales elegidos para replicar los ejemplos:
# < $1,000  => BAJAS
# [ $1,000 , $3,000 ) => MODERADAS
# >= $3,000 => BUENAS
if ingresos_totales < 1000:
    print("La función generó BAJAS ganancias.")
elif ingresos_totales < 3000:
    print("La función generó ganancias MODERADAS.")
else:
    print("La función generó BUENAS ganancias.")

"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

[Respuesta]
- Se realiza una pregunta al usuario antes de calcular el precio: "¿Es martes? (S/N)" o "Indica el día de la semana".
- Variables: agrega una bandera, por ejemplo `es_martes = input("¿Es martes? (S/N): ").lower() == "s"`.
- Lógica: justo en la sección donde determinas `precio_boleto` para Adulto (dentro del if tipo_op == "2"),
  aplica el descuento:
      `precio_boleto = PRECIO_ADULTO * (0.8 if es_martes else 1.0)`
  y usa ese `precio_boleto` para actualizar `ingresos_adultos` y `ingresos_totales`.
- Consideración: Mantén los demás tipos sin descuento para no alterar otras estadísticas.

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

[Respuesta]
Si el total general siempre sale incorrecto, aunque los ingresos por tipo estén bien, haría esto paso por paso:
1. Revisar que el total empiece en cero
Verificar que ingresos_totales = 0.0 esté bien escrito y que no se vuelva a poner en cero dentro del ciclo por error.

2. Revisar dónde se suma el total
Confirmar que en cada venta se esté haciendo:
ingresos_totales += precio_boleto
y que realmente se esté usando el precio correcto.

3. Verificar que todos usen el mismo precio
Asegurarme de que los ingresos por tipo (adultos, estudiantes, etc.) estén usando el mismo valor que se sumó al total, especialmente si hay descuentos.

4. Agregar mensajes de prueba (debug)
Pondría un print temporal después de sumar al total, por ejemplo:
print("Precio:", precio_boleto, "Total acumulado:", ingresos_totales)
Así puedo ver si el número va creciendo correctamente.

5. Comprobar que no se reinicie el total sin querer
Revisar que en ninguna parte del código se esté reiniciando la variable por error.

6. Verificar que se esté imprimiendo la variable correcta
Asegurarme de que al final se esté mostrando ingresos_totales y no otra variable parecida.

7. Comparar con una suma manual
Haría una suma aparte de todos los ingresos por tipo:
ingresos_estudiantes + ingresos_adultos + ingresos_tercera_edad + ingresos_academicos
y la compararía con el total general.
Si no coinciden, entonces el error está en alguna parte donde se están sumando los valores.
"""