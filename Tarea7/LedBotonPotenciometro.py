import serial
import tkinter as tk
import threading

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
ser = serial.Serial('COM4', 9600)

# Variable global para el texto del potenciómetro
pot_value_text = None

# Función para leer datos del puerto serie en un hilo separado
def serial_reader():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                handle_code(data)

# Función para encender un círculo
def turn_on_circle(circle, color):
    canvas.itemconfig(circle, fill=color)

# Función para apagar un círculo
def turn_off_circle(circle):
    canvas.itemconfig(circle, fill="white")

# Función para manejar los datos recibidos del puerto serie
def handle_code(code):
    try:
        digit = int(code)
        print("Arduino:", digit)
        # Apagar todos los círculos primero
        for circle in circles:
            turn_off_circle(circle)

        # Encender el círculo correspondiente al código recibido
        if digit == 2:
            turn_on_circle(circles[0], "green")
        elif digit == 4:
            turn_on_circle(circles[1], "yellow")
        elif digit == 6:
            turn_on_circle(circles[2], "red")
        # Actualizar el valor de la barra de potenciómetro
        update_bar_graph(digit)
    except ValueError:
        print("Arduino:", code)

# Función para actualizar la barra de potenciómetro
def update_bar_graph(value):
    global pot_value_text
    # Normalizar el valor para que esté en el rango de 0 a 1 (Tkinter no acepta valores fuera de este rango)
    normalized_value = value / 1023
    # Calcular las coordenadas de la barra
    x0 = 50
    y0 = 450 - normalized_value * 300  # Reducir la altura de la barra
    x1 = 100
    y1 = 450
    # Actualizar las coordenadas y el color de la barra
    canvas.coords(bar, x0, y0, x1, y1)
    
    # Actualizar el texto del potenciómetro
    if pot_value_text:
        canvas.delete(pot_value_text)  # Eliminar el texto existente
    pot_value_text = canvas.create_text(75, 130, text=f"{value}", font=("Comic Sans MS", 10), anchor=tk.CENTER)

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("2do Examen Parcial")
root.geometry("500x500")  # Ajustar el tamaño de la ventana

# Configuración de la gráfica de barras
canvas = tk.Canvas(root, width=300, height=350, bg='medium turquoise')  # Ajustar el tamaño del lienzo
canvas.pack()
bar = canvas.create_rectangle(50, 450, 100, 450, fill='cyan')  # Rectángulo que representa la barra de potenciómetro
canvas.create_text(75, 100, text=f"", font=("Comic Sans MS", 12), anchor=tk.CENTER)  # Nombre del potenciómetro

circles = []
for i in range(3):
    circle = canvas.create_oval(25 + i * 100, 50, 75 + i * 100, 100, outline="black", width=2)  # Ajustar la posición de los círculos
    canvas.create_text(50 + i * 100, 75, text=str(i+1), font=("Comic Sans MS", 12))  # Ajustar la posición del texto
    circles.append(circle)

canvas.create_text(265, 223, text="PreOrden", font=("Comic Sans MS", 10), anchor=tk.CENTER)
canvas.create_text(265, 243, text="InOrden", font=("Comic Sans MS", 10), anchor=tk.CENTER)
canvas.create_text(265, 263, text="PostOrden", font=("Comic Sans MS", 10), anchor=tk.CENTER)

# Crear y ejecutar el hilo para leer datos del puerto serie
serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

# Ejecutar la aplicación Tkinter
root.mainloop()