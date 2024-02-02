#0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
#Define una función que tome dos parámetros y devuelva True si la suma de ambos es par y False si es impar.

def parImpar(num1, num2):
    suma = num1 + num2
    return suma % 2 == 0

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

esPar = parImpar(num1, num2)

if esPar:
    print(f"Los numeros ingresados por el usuario son: {num1} y {num2}\nLa suma de dichos numeros es igual a: {num1 + num2} y es un numero PAR True")
else:
    print(f"Los numeros ingresados por el usuario son: {num1} y {num2}\nLa suma de dichos numeros es igual a: {num1 + num2} y es un numero IMPAR False")
