'''
Escribir una función en Python que tome una cadena de paréntesis y determine si están balanceados.
Utilizar una pila para rastrear la apertura y cierre de paréntesis.
'''
#funcion de parentesis balanceados
def parentesisBalanceados(cadena):

    Pila = [] #Lista vacia para rastrear los paréntesis de apertura

    for caracter in cadena:
        if caracter == '(':
            Pila.append(caracter) # Agregar paréntesis de apertura a la pila
        elif caracter == ')':
            if not Pila or Pila.pop() != '(': # Verificar si hay paréntesis de cierre sin su correspondiente apertura
                return False
    return not Pila #La cadena está balanceada si la pila está vacía al final

#Cadenas
cadena1 = "()" #True
cadena2 = ")([]{}" #False
cadena3 = ")(" #False
cadena4 = ")[()]" #False
cadena5 = "{[]}" #True

print(parentesisBalanceados(cadena1))
print(parentesisBalanceados(cadena2))
print(parentesisBalanceados(cadena3))
print(parentesisBalanceados(cadena4))
print(parentesisBalanceados(cadena5))