'''import serial, time, tkinter

arduino = serial.Serial('COM4', 9600)

#Hacer que el usuario ingrese el numero 
while True:

    ingresoNum = input("Ingrese el valor que desea enviar al arduino (ingresar 's o S' para salir): ")

    #usa metodos para salir del programa
    if ingresoNum.lower() == 's':
        print("Saliendo del programa...")
        break

    #esto sirve para que el usuario ingrese el caracter
    arduino.write(str.encode(ingresoNum))

    print("Valor enviado correctamente ;)")

arduino.close()#cerrar el serial
'''

import tkinter as tk
import serial

# Inicializar la comunicación serial con Arduino
arduino = serial.Serial('COM4', 9600)  # Reemplaza 'puerto_serial_de_arduino' con el puerto correcto

# Función para procesar los datos recibidos de Arduino
def procesar_datos(datos):
    if datos.startswith('Grupo Led'):
        # Actualizar el estado de los LEDs en el dashboard
        # Puedes implementar esta parte según tus preferencias y diseño de la interfaz
        pass
    elif datos.startswith('Boton'):
        # Actualizar el estado de los botones en el dashboard
        # Puedes implementar esta parte según tus preferencias y diseño de la interfaz
        pass

# Función para enviar comandos a Arduino
def enviar_comando(comando):
    arduino.write(comando.encode())

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Dashboard")

# Centrar la ventana en la pantalla
ancho_ventana = 700
alto_ventana = 100
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2
ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}')

# Crear un contenedor para los botones y organizarlos horizontalmente
frame_botones = tk.Frame(ventana)
frame_botones.pack()

def boton_presionado(comando):
    enviar_comando(comando)

# Ejemplo de creación de botones
boton_A = tk.Button(frame_botones, text="Prender 1er Grupo", command=lambda: boton_presionado('A'))
boton_A.pack(side=tk.LEFT, padx=5, pady=5)

boton_B = tk.Button(frame_botones, text="Prender 2do Grupo", command=lambda: boton_presionado('B'))
boton_B.pack(side=tk.LEFT, padx=5, pady=5)

boton_C = tk.Button(frame_botones, text="Prender 3er Grupo", command=lambda: boton_presionado('C'))
boton_C.pack(side=tk.LEFT, padx=5, pady=5)

boton_D = tk.Button(frame_botones, text="Prender 4to Grupo", command=lambda: boton_presionado('D'))
boton_D.pack(side=tk.LEFT, padx=5, pady=5)

boton_E = tk.Button(frame_botones, text="Apagar TODOS los Grupo", command=lambda: boton_presionado('E'))
boton_E.pack(side=tk.LEFT, padx=5, pady=5)

# Bucle principal para recibir y procesar datos de Arduino
def leer_datos_desde_arduino():
    while True:
        datos = arduino.readline().decode().strip()
        if datos:
            procesar_datos(datos)

# Crear un hilo para leer datos de Arduino en segundo plano
import threading
thread_arduino = threading.Thread(target=leer_datos_desde_arduino)
thread_arduino.start()

# Iniciar el bucle de la interfaz de usuario
ventana.mainloop()
