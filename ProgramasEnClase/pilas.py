cartas = [] #letters

#permitir inssertar datos a la lista
cartas.append('C')#0
cartas.append('A')#1
cartas.append('T')#2
cartas.append('G')#3

print(cartas, "\n")

#extraer datos
ultimoElemento = cartas.pop(0)
print(ultimoElemento, "\n")

ultimoElemento = cartas.pop(2)
print(ultimoElemento, "\n")

print(cartas, "\n")