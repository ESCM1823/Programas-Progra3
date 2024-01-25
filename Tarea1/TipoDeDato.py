# 0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
# Un programa que indique en que tipo de dato se debe ingresar esa variable.
dato = input("Ingrese cualquier dato: ")

try:
    num = eval(dato)
    var = type(num).__name__
    print("La entrada es de tipo:", var)
except:
    var = type(dato).__name__
    print("La entrada es de tipo:", var)

if var == "int":
    print("¡La entrada es un número entero!")
elif var == "float":
    print("¡La entrada es un número decimal!")
elif var == "str":
    print("¡La entrada es una cadena de texto!")
elif var == "bool":
    print("¡La entrada es de tipo booleana!")
else:
    print("¡Tipo de dato no identificado!")