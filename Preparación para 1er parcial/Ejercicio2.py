'''
Escriba un programa de Python para encontrar el valor mas cercano de un valor objetivo dado
en un arbol de busqueda binaria (BST) no vacio dado de valores unicos.
'''
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def closest_value(root, target):
    a = root.val
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = closest_value(kid, target)
    return min((a,b), key = lambda x: abs(target - x))

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

result = closest_value(root,19)
print(result)