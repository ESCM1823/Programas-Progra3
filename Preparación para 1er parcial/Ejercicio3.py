'''
Escriba un programa Python para verificar si un arbol binario dado es un arbol de busqueda
binaria (BST) valido o no.
a. Dejeque un arbol de busqueda binaria (BST) se defina de la siguiente manera:
    i. El subarbol izquierdo de un nodo contiene solo nodos con claves menores que la
    clave del nodo.
    ii. El subarbol derecho de un nodo contiene solo nodos con claves mayores que la
    clave del nodo.
    iii. Los subarboles izquierdo y derecho también deben ser arboles de busqueda
    binarios.
'''
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def is_BST(root):
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.val <= prev.val:
            return False
        prev = root
        root = root.right
    return True

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = is_BST(root)
print(result)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

result = is_BST(root)
print(result)