# 0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
# Un programa que opere la formula cuadrática.
import math # libreria

print("Recuerda que para la formula cuadratica la ecuacion tiene que ser de grado dos")

#ingreso de datos
valorA = int(input("Ingrese el valor de A: "))
valorB = int(input("Ingrese el valor de B: "))
valorC = int(input("Ingrese el valor de C: "))

valorRaiz = valorB**2 - 4 * valorA * valorC #formula que va dentro de la raiz

if valorRaiz >= 0:
    # Dos soluciones reales
    x1 = (-valorB + math.sqrt(valorRaiz)) / (2 * valorA)
    x2 = (-valorB - math.sqrt(valorRaiz)) / (2 * valorA)
    print("Las soluciones reales son:")
    print("X1 =", x1)
    print("X2 =", x2)
else:
    # Soluciones complejas
    parteReal = -valorB / (2 * valorA)
    parteImaginaria = math.sqrt(abs(valorRaiz)) / (2 * valorA)
    solucion1 = complex(parteReal, parteImaginaria)
    solucion2 = complex(parteReal, -parteImaginaria)
    print("Las soluciones complejas son:")
    print("X1 =", solucion1)
    print("X2 =", solucion2)