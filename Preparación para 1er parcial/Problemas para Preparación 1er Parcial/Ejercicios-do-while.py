'''
Do-While:

Problema: Escribir un programa que pida al usuario adivinar un número del 1 al 10. Utiliza un bucle do-while para repetir la solicitud hasta que el usuario adivine correctamente.
'''

#libreria random
import random

num = random.randint(1, 10)

while num:

    ingresoValor = int(input("Adivina el numero: "))
    
    if ingresoValor > num:
        print(f"CASI ya no puedes usar este numero: {ingresoValor} intenta con uno menor")
    elif ingresoValor < num:
        print(f"CASI ya no puedes usar este numero: {ingresoValor} intenta con uno mmayor")
    else:
        print(f"FELICIDADES EL NUEMRO ERA: {num} ADIVINASTE EL NUEMRO")
        break