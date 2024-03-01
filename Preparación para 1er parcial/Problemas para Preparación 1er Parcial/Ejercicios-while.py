'''
While:
Problema: Escribir un programa que solicite al usuario un número y luego imprima todos los números pares desde 0 hasta ese número utilizando un bucle while.
'''

inicio = 0 #iniciador
ingresoNumero = int(input("Ingresa el numero que quiere llegar: "))

while inicio <= ingresoNumero:
    print(inicio)
    inicio += 2 #inicio = inicio + 2