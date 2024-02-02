#0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
#Crea una clase llamada "Estudiante" con atributos como nombre, edad y calificación. Implementa un método en la clase para verificar si el estudiante ha aprobado o no (calificación mayor o igual a 60).
class Estudiante:
    
    # Constructor que inicializa los atributos cuando se instancia la clase.
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    # Método para determinar si el estudiante ha aprobado.
    def aprobado(self):
        return self.calificacion >= 60

# Fin de la definición de la clase Estudiante

# Solicitar al usuario que ingrese los atributos del estudiante.
nomEstudiante = input("Ingrese el nombre del estudiante: ")
edadEstudiante = int(input("Ingrese la edad del estudiante: "))
calificacionEstudiante = int(input("Ingrese la calificación del estudiante: "))

# Crear una instancia de la clase Estudiante con los atributos ingresados por el usuario.
varEstudiante = Estudiante(nomEstudiante, edadEstudiante, calificacionEstudiante)

# Verificar si el estudiante ha aprobado
if varEstudiante.aprobado():
    print(f"El estudiante: {varEstudiante.nombre}\nCon edad de: {varEstudiante.edad}\nCon calificacion: {varEstudiante.calificacion} ha Aprobado.")
else:
    print(f"El estudiante: {varEstudiante.nombre}\nCon edad de: {varEstudiante.edad}\nCon calificacion: {varEstudiante.calificacion} ha Reprobado.")