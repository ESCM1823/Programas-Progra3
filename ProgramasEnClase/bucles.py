#while = SI sabemos de cuantas veces se va a realizar el ciclo / mientras se cumple la condicion se va a repetir el ciclo
#do-while = NO sabemos de cuantas veces se va a realizar el ciclo / se va a repetir el ciclo hasta que se cumpla la condicion
#for = SI sabemos de cuantas veces se va a realizar el ciclo

# Ejemplo de bucle while que imprime números del 1 al 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Ejemplo de bucle do-while simulado que solicita al usuario un número mayor que 10
numero = 0
while True:
    numero = int(input("Ingrese un número mayor que 10: "))
    if numero > 10:
        break
    else:
        print("El número ingresado no es mayor que 10. Inténtelo de nuevo.")

# Ejemplo de bucle for que recorre una lista de colores
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)
