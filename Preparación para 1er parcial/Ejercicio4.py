'''
Escriba un programa de Python para eliminar un nodo con la clave dada en un arbol de
busqueda binario (BST) dado.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def delete_Node(root, key):
    if not root:
        return root

    if root.val > key:
        root.left = delete_Node(root.left, key)
    elif root.val < key:
        root.right = delete_Node(root.right, key)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        
        temp_val = root.right
        mini_val = temp_val.val
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.val
        root.right = deleteNode(root.right, root.val)
    return root

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(7)
print(f"Nodo original: {preOrder(root)}")
result = delete_Node(root, 4)
print(f"Despues de eliminar el nodo especifico: {preOrder(result)}")