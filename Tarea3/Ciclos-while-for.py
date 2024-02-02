#0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
#Desarrolla un programa que imprima los primeros 10 números pares utilizando un ciclo while o for.

#bucle while
contador = 2

print("imprimir los primeros 10 numeros pares con el ciclo while")

while contador <= 20:
    print(contador)
    contador += 2

'''
#bucle for se utiliza para iterar sobre secuencias como listas, tuplas, cadenas, etc., pero no para iterar sobre un número directamente.
for num in contador:
    print (num)
'''

#bucle for
print("\nimprimir los primeros 10 numeros pares con el ciclo for")

for num in range(2, 21, 2):  # Comienza en 2, termina en 20, incremento de 2
    print(num)