'''
If y If-Else:
Problema: Escribir un programa que determine si un número ingresado por el usuario es positivo, negativo o cero.
'''

ingresoNumero = int(input("Ingrese un numero entero: "))

if  ingresoNumero > 0:
    print(f"El numero: {ingresoNumero} es positivo")
elif ingresoNumero < 0:
    print(f"El numero: {ingresoNumero} es negativo")
else:
    print(f"El numero: {ingresoNumero} es cero")