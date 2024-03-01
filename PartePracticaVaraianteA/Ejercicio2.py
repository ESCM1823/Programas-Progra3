'''
0901-22-940-Edwin Stevens Cambranes Mendizábal
Define una función llamada "inverso_palabra" que reciba una cadena
como parámetro y devuelva la
cadena invertida. Por ejemplo, si la entrada es "python", la salida
debería ser "nohtyp".
'''
def inverso_palabra():

    palabra = input("Ingresa una palabra: ")#ingreso de la palabra

    lista = []#creo una lista vacia

    #ciclo que agrega la palabra luego el metodo reverse lo revierte letra por letra
    for letra in palabra:
        lista.append(letra)
    lista.reverse()

    palabra_invertida = "" #detecta los espacios en blanco

    #luego agrega las letras solo que en orden revertido
    for letra in lista:
        palabra_invertida += letra
    print(palabra_invertida)
    
#llamando a la función
inverso_palabra()
