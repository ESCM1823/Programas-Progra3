#clase llamada Node
class Node:
    #funcion inicial o principal (parametro self valor reservado, parametro valor)
    def __init__(self, valor):
        #estructura de un arbol
        self.valor = valor
        self.izquierdo = Node
        self.derecho = Node

#instansear clase
raiz = Node(1) #valor del nodo = 1
raiz.izquierdo = Node(2)
raiz.derecho = Node(3)

#sub nodo
raiz.izquierdo.izquierdo = Node(4)

#sub sub nodo
raiz.izquierdo.izquierdo.izquierdo = Node(5)