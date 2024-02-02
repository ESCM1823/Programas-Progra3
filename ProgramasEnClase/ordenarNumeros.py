entrada_ususario = input("Ingresa los numeros a ordenar separados por espacios: ")

lista_de_numeros = [float(x) for x in entrada_ususario.split()]
print(lista_de_numeros)

lista_de_numeros.sort()

print(lista_de_numeros)