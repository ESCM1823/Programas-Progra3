#lista
numero = [1,2,3,4,5,6,7,8,9]

#Diccionarios
personas = {
    "Juan": 20,
    "Maria": 30,
    "Profesion":"Ingeniero"
}

edades = {"Juan":30, "Maria":20, "Pedro":18}

#Ejemplo de pila
pila = []

pila.append(1)
print(pila)
sacarElemento = pila.pop()
print("Pila sin elementos: ", pila)

#Ejemplo de cola
from collections import deque

cola = deque([1,2,3,4,5])

for valor in cola:
    print("\nElementos de la cola: ", valor)

elementosSacar = cola.popleft()

for valor in cola:
    print("\nElemento sacado de la cola: ", valor)