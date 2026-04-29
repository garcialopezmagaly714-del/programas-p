# p148-nombres.py
# Escribe una función que tome dos listas de nombres, las una, invierta el orden y convierta todos los nombres a mayúsculas

from typing import List

def une_procesa(l1: List[str], l2: List[str]) -> List[str]:
    todo = l1 + l2
    todo.sort()
    may : List[str] = []
    for nombre in todo:
        may.append(nombre.upper())
    return may

def entrda() -> List[str]:
    datos = []
    print("Introduce nombres (deja en blanco para terminar):")
    while True:
        nombre = input("Nombre: ")
        if nombre == "": break
        datos.append(nombre)
    return datos

nombres1 : List[str] = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]
nombres2 : List[str] = entrda()
todo     : List[str] = une_procesa(nombres1, nombres2)

print(f"Lista nombres 1: {nombres1} - {len(nombres1)}")
print(f"Lista nombres 2: {nombres2} - {len(nombres2)}")
print(f"Todo: {todo} - {len(todo)}")