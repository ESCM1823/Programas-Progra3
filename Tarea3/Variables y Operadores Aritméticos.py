#0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
#Escribe un programa que solicite al usuario ingresar dos números y luego muestre la suma, resta, multiplicación y división de esos números.

#El usuario ingresa valores
num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa otro numero entero: "))

#variables aritmeticas
sum = num1 + num2
res = num1 - num2
mul = num1 * num2
div = num1 / num2


#salida de datos
print(f"La suma de los numeros: {num1} y {num2} es igual a: {sum}")
print(f"La resta de los numeros: {num1} y {num2} es igual a: {res}")
print(f"La multiplicacion de los numeros: {num1} y {num2} es igual a: {mul}")
print(f"La division de los numeros: {num1} y {num2} es igual a: {div}")