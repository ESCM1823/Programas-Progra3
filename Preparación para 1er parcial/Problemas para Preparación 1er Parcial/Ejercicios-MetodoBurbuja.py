arreglo = [23,6,4,3,54,54,34]
print("Arreglo no ordenado: ",arreglo)
n = len(arreglo)
print(n)
contador_de_intercambios = 1

intercambio = True

while (intercambio):
    intercambio = False
    for i in range(1,n):
        if arreglo[i-1]>arreglo[i]:
            arreglo[i-1],arreglo[i] = arreglo[i], arreglo[i-1]
            intercambio = True
            contador_de_intercambios+=1
            print(contador_de_intercambios)
    n-=1

print("Arreglo ordenado: ",arreglo)