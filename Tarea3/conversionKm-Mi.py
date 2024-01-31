#0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
#convertir una distancia en Kilómetros a una distancia en millas

'''

ingresoKm = float(input("Ingresa la distancia en Kilómetros: "))
#condicion
if (ingresoKm < 0):
    print("Ingresa un valor coherente (numero mayor a 0)")
else:
    convertir = ingresoKm / 1.609
    print("El valor ingresado fue de: ", ingresoKm, "Km y su conversion a millas es de: ", convertir, "millas")

'''

#Segunda opcion de resolver dicho programa

#funcion que se llama kmNegativo y va a almacenar la variable KM que dice que va a ser km mayor que 0
def kmNegativo(KM):
    return KM > 0

try:
    ingresoKm = float(input("Ingresa la distancia en Kilómetros: "))

    #llamo a la funcion y le digo que tome el valor de la variable ingresoKm
    if kmNegativo(ingresoKm):
        millas = ingresoKm / 1.609 #formula
        # Redondear las millas a dos decimales para una presentación más limpia
        print(f"El valor ingresado fue de: {ingresoKm} Km y su conversión a millas es de: {round(millas, 2)} millas")
    else:
        print(f"El valor ingresado fue de: {ingresoKm} Km. Recuerda que los Km no pueden ser negativos.")

except ValueError:
    print("Ingresa un kilometraje para poder convertir el valor a millas")