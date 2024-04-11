import serial
import tkinter as tk

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
ser = serial.Serial('COM4', 9600)

# Función para actualizar la gráfica de barras y el valor del potenciómetro
def update():
    # Leer dato del puerto serial
    data = ser.readline().decode().strip()
    value = int(data)
    print(data)
    
    # Normalizar el valor para que esté en el rango de 0 a 100 (Tkinter no acepta valores fuera de este rango)
    normalized_value = int((value / 1023) * 100)
    
    # Actualizar la altura de la barra
    canvas.coords(bar, 5, 105 - normalized_value, 35, 105)

    # Actualizar el valor del potenciómetro
    pot_label.config(text=f"{value}")

    # Actualizar la ventana
    root.update_idletasks()
    root.update()

#ventana de Tkinter
root = tk.Tk()
root.title("Arduino Data Plotter")

# Etiqueta para mostrar el valor del potenciómetro
pot_label = tk.Label(root, text="", font=("Arial", 12))
pot_label.place(x=7, y=70)  # Colocar en la esquina superior izquierda

# Dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Coordenadas para centrar la ventana
x = (screen_width - 400) // 2  # El ancho de la ventana es 400
y = (screen_height - 200) // 2  # La altura de la ventana es 200
root.geometry(f"400x200+{x}+{y}")

# Gráfica de barras
canvas = tk.Canvas(root, width=40, height=105, bg='Gray')
canvas.place(x=0, y=95)  # Colocar la gráfica en la esquina inferior izquierda
bar = canvas.create_rectangle(5, 105, 35, 105, fill='Green')

# Configurar un temporizador para actualizar la gráfica y el valor del potenciómetro periódicamente
while True:
    update()

# Ejecutar la aplicación Tkinter
root.mainloop()