#simulando una linea de espera en un banco = ejemplo de COLA

from collections import deque
import time

def simularLineaEspera(clientesEspera):

    queue = deque(clientesEspera)#cola

    print(queue, "\n")

    while queue:
        print("Atendiendo al clinete: ", queue.popleft())
        time.sleep(1)#demora 1 segundo

clientesEspera = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4"]#lista

print("Bienvenido al banco, se les estara atendiendo segun este orden ;) \n")
simularLineaEspera(clientesEspera)
print("Todos los clientes fueron atendidos \n")