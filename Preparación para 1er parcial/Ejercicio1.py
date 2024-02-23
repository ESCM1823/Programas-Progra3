'''
Escriba un programa de Python para crear un arbol de busqueda binaria equilibrada utilizando
elementos de una matriz (dados) donde los elementos de la matriz se ordenan en orden
ascendente.
'''
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def sorted_array_to_bst(nums):

    if not nums:
        return None
    mid_val = len(nums)//2
    node = TreeNode(nums[mid_val])
    node.left = sorted_array_to_bst(nums[:mid_val])
    node.right = sorted_array_to_bst(nums[mid_val+1:])
    return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

result = sorted_array_to_bst([1,2,3,4,5,6,7])
preOrder(result)