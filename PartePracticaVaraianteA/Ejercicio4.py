'''
0901-22-940-Edwin Stevens Cambranes Mendizábal
Crea un diccionario en Python que represente un libro, con claves como
"título", "autor" y "año de publicación". Luego, escribe un código que agregue un nuevo campo al
diccionario, como "género", y lo imprima.
'''

libro = ["titulo", "autor", "año de publicación"]

libro.append("genero")  # Agregar el género del libro a la lista
libro.append("numero de paginas")

print(libro)