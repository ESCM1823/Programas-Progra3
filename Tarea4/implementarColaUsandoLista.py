'''
Definir funciones para las operaciones básicas de una cola: enqueue (añadir elemento), dequeue (eliminar
elemento) y front (ver el primer elemento sin eliminarlo).
Escribir un programa que simule el proceso de atención en una fila, donde los elementos son atendidos en
el orden en que llegan.
'''
from collections import deque #libreria
#crear una clase Cola para ordenar mejor todo
class Cola:
    #funcion inicial con lista vacia
    def __init__(self):
        self.listaVacia = []
    
    #funcion poner en cola
    def enqueue(self, elemento):
        self.listaVacia.append(elemento)
    
    #funcion sacar de cola
    def dequeue(self):
        if not self.colaVacia():
            return self.listaVacia.pop(0) #Esta línea elimina y devuelve el primer elemento de la lista que representa la cola. 
        else:
            return None #Devolver None si la cola esta vacia

    # Su propósito es ver el primer elemento en la cola sin eliminarlo.
    def front(self):
        if not self.colaVacia():
            return self.listaVacia[0] #Devuelve el primer elemento de la cola
        else:
            return None #Devolver None si la cola esta vacia
    
    def colaVacia(self):
        return len(self.listaVacia) == 0 #la función colaVacia() devuelve True si la cola está vacía y False si la cola tiene al menos un elemento.

#proceso de atención en una fila
def atencionFila(elementos):
    fila = Cola() #se convierte en una instancia de la clase Cola.

    #agregar elementos a la fila
    for elemento in elementos:
        fila.enqueue(elemento)

    print("Proceso de atencion en la fila: ")
    while not fila.colaVacia():
        #atender al proximo cliente
        siguienteElemento = fila.dequeue()
        print(f"Atendiendo: {siguienteElemento}")

    if fila.colaVacia():
        print("Todos los Clientes han sido atendidos ;)")

#Clientes dentro de la lista
elementos = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]
atencionFila(elementos)