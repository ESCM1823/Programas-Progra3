'''
Implementar una pila utilizando una lista en Python.
Crear funciones para realizar las operaciones básicas de una pila: push (añadir elemento), pop (eliminar
elemento) y peek (ver el elemento superior sin eliminarlo).
Escribir un programa que utilice esta pila para invertir el orden de una lista dada.
Implementación de una Cola (Queue):
'''
#Crear Clase Pila
class Pila:
    #funciones para realizar las operaciones basicas
    def __init__(self):
        self.lista = [] #lista vacia

    #funcion push sirve para añadir elemento a la lista
    def push(self, elemento):
        self.lista.append(elemento)
    
    #Este metodo se utiliza para eliminar y devolver el elemento en la parte superior de la pila.
    def pop(self):
        if not self.pilaVacia():
            return self.lista.pop()
        else:
            return None #Devolver None si la pila esta vacia
    
    #Este metodo devuelve el elemento en la parte superior de la pila sin eliminarlo.
    def peek(self):
        if not self.pilaVacia():
            return self.lista[-1] #Devuelve el último elemento de la lista
        else:
            return None #Devolver None si la pila esta vacia
    
    #la función colaVacia() devuelve True si la cola está vacía y False si la cola tiene al menos un elemento.
    def pilaVacia(self):
        return len(self.lista) == 0 #len es una función integrada de Python que te permite obtener el número de elementos de varios tipos de objetos.

# Función para invertir el orden de una lista utilizando la pila
def invertir_lista(lista):
    pila = Pila() #Se crea una instancia de la clase Pila
    for elemento in lista:
        pila.push(elemento) #Esto significa que los elementos se agregan a la pila en el orden inverso al original.

    lista_invertida = [] #lista vacia

    while not pila.pilaVacia():
        lista_invertida.append(pila.pop())

    return lista_invertida

# Ejemplo de uso:
lista_original = [1, 2, 3, 4, 5]
print("Lista original:", lista_original)

lista_invertida = invertir_lista(lista_original) #aqui llamo a la funcion invertir lista y creo su instancia
print("Lista invertida:", lista_invertida)