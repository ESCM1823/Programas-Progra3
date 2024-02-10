'''
Desarrollar una clase ColaConPilas que utilice dos pilas para simular el comportamiento de una cola.
Implementar las operaciones enqueue y dequeue utilizando las operaciones de pilas.
'''
from collections import deque #libreria

class ColaConPilas:
    
    def __init__(self):
        self.pilaEntrada = [] #pila para encolar elementos
        self.pilaSalida = [] #pila para desencolar elementos

    def enqueue (self, elemento):
        self.pilaEntrada.append(elemento) #Agregaar elementos la pila entrada
    
    def dequeue(self):
        if not self.pilaSalida: #si es null pilaSalida
            while self.pilaEntrada:
                self.pilaSalida.append(self.pilaEntrada.pop()) # función de transferir los elementos de la pila de entrada a la pila de salida en orden inverso.
        if self.pilaSalida: # Si la pila de salida tiene elementos, desencolar el elemento superior
            return self.pilaSalida.pop()
        else: # Si ambas pilas están vacías, la cola está vacía
            return None

cola = ColaConPilas() #instanciar
#Ingresar Datos a la cola
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(30)

print(cola.dequeue()) #1
print(cola.dequeue()) #2
print(cola.dequeue()) #3
print(cola.dequeue()) #4
print(cola.dequeue()) #30
print(cola.dequeue()) #None
print(cola.dequeue()) #None