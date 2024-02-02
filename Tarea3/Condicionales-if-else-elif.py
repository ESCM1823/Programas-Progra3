#0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
#Crea un programa que determine si un número ingresado por el usuario es positivo, negativo o cero.

#El usuario ingresa valores
numUsuario = int(input("Ingresa cualquier numero entero que desees: "))

if numUsuario >= 1:
    print(f"El numero: {numUsuario} es Positivo")
elif numUsuario <= -1:
    print(f"El numero: {numUsuario} es Negativo")
else:
    print(f"El numero: {numUsuario} es Cero")