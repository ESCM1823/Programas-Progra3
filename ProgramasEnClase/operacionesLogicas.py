#ejemplo de operacion and
condicion_and = ( 5 > 3) and (10 < 20)
print(condicion_and)

#ejemplo de operador or
condicion_or = (5 > 3) or (10 > 20)
print(condicion_or)

#funcion
def puede_votar(edad):
    return edad >= 18

#try utiliza para capturar errores en el codigo y except para manejarlos
try:
    edad_usuario = int(input("Ingrese tu edad: "))
    if puede_votar(edad_usuario):
        print("Puedes votar")
    else:
        print("No puedes votar")
except ValueError:
    print("Debes ingresar una edad valida")