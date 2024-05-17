import serial
import tkinter as tk

# Iniciar la comunicación serial
ser = serial.Serial('COM4', 9600, timeout=1)

# Crear la ventana principal
root = tk.Tk()
root.title("Lab 10")
root.configure(bg='darkblue')

# Centrar la ventana
ancho_ventana = 250
alto_ventana = 250
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2
root.geometry(f'{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}')

# Crear un label para los mensajes de depuración
mensaje_label = tk.Label(root, text="", bg='darkblue', fg='white', wraplength=200, justify=tk.LEFT, font=("Arial", 10))
mensaje_label.pack()

# Crear un frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(expand=True)
frame_botones.configure(bg='darkblue')

# Limite de líneas para los mensajes
limite_lineas = 10

# Función para enviar comandos a Arduino
def enviar_comando(comando):
    ser.write(comando.encode())

# Función para manejar el evento de presionar un botón
def boton_presionado(comando):
    enviar_comando(comando)
    limpiar_label()

# Función para limpiar el label
def limpiar_label():
    mensaje_label.config(text="")

# Función para leer los mensajes de depuración del puerto serial
def leer_mensajes():
    if ser.in_waiting > 0:
        mensaje = ser.readline().decode('utf-8').strip()
        # Obtener el texto actual y agregar el nuevo mensaje
        texto_actual = mensaje_label.cget("text")
        lineas = texto_actual.split("\n")
        if len(lineas) >= limite_lineas:
            lineas = lineas[1:]  # Eliminar la línea más antigua
        lineas.append(mensaje)
        nuevo_texto = "\n".join(lineas)
        mensaje_label.config(text=nuevo_texto)
    root.after(100, leer_mensajes)

# Crear los botones
botonStepper = tk.Button(frame_botones, text="Iniciar Stepper", command=lambda: boton_presionado('1'), font=("Arial", 10))
botonStepper.pack(side=tk.LEFT, padx=5, pady=5)
botonStepper.configure(bg='white')

botonServo = tk.Button(frame_botones, text="Iniciar Servo", command=lambda: boton_presionado('2'), font=("Arial", 10))
botonServo.pack(side=tk.LEFT, padx=5, pady=5)
botonServo.configure(bg='white')

# Iniciar la lectura de mensajes
leer_mensajes()

# Iniciar el bucle principal de Tkinter
root.mainloop()
