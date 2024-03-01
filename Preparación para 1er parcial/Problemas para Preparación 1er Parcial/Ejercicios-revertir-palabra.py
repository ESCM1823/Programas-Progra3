# Solicitar al usuario que ingrese una cadena
cadena = input("Ingrese una cadena: ")

# Invertir la cadena utilizando slicing
#indica que se toma la cadena desde el principio hasta el final, pero con un paso de -1, lo que invierte el orden de los caracteres.
cadena_invertida = cadena[::-1]

# Imprimir la cadena invertida
print("Cadena invertida:", cadena_invertida)