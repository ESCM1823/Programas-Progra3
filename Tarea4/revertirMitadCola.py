'''
Escribir una función que tome una cola y revierta la mitad de sus elementos utilizando solo una pila
adicional.
La cola debe mantener la misma secuencia de elementos, pero la mitad debe estar en orden inverso.
'''
from collections import deque

def revertirMitad(cola):
    pila = []

    longitud = len(cola)
    mitad = longitud // 2
    
    #simplemente indica que estamos iterando mitad veces, pero no estamos utilizando los valores del índice en el bucle. 

    # Transferir la mitad de la cola a la pila
    for _ in range(mitad):
        pila.append(cola.popleft())
    
    # Transferir la mitad de la pila a la cola en orden inverso
    for _ in range(mitad):
        cola.appendleft(pila.pop())

    # Si la longitud de la cola es impar, omitir el elemento central
    if longitud % 2 != 0:
        cola.append(cola.popleft())
    
    return cola

# Datos de ejemplo
enCola = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Cola original:", enCola)
revertirMitad(enCola)
print("Cola con la mitad revertida:", enCola)