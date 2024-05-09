import serial
import tkinter as tk

# Configurar el puerto serial
ser = serial.Serial('COM4', 9600)

def actualizar_etiqueta():
    if ser.in_waiting > 0:
        datos = ser.readline().decode().strip()
        etiqueta_serial.config(text=datos)
        if datos == "Rele ON":
            canvas_led.itemconfig(circulo_led, fill="red")  # Cambiar color del círculo a rojo (simula LED encendido)
        elif datos == "Rele OFF":
            canvas_led.itemconfig(circulo_led, fill="grey")  # Cambiar color del círculo a gris (simula LED apagado)
    root.after(100, actualizar_etiqueta)

def toggle_rele():
    ser.write(b't')  # Enviar 't' a Arduino para alternar el estado del relé

root = tk.Tk()
root.title("Lab 9")

# Centrar la ventana en la pantalla
ancho_ventana = 200
alto_ventana = 200
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2
root.geometry(f'{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}')

# Etiqueta para el mensaje serial del Arduino
etiqueta_serial = tk.Label(root, text="")
etiqueta_serial.pack(side=tk.TOP)  # Mostrar la etiqueta en la parte superior

# Canvas para simular el LED como un círculo
canvas_led = tk.Canvas(root, width=100, height=100, bg="white")
canvas_led.pack(side=tk.TOP)  # Mostrar el canvas en la parte superior

# Dibujar el círculo (LED) en el canvas
x1, y1, x2, y2 = 10, 10, 90, 90  # Coordenadas para el círculo
circulo_led = canvas_led.create_oval(x1, y1, x2, y2, outline="black", fill="grey")

# Botón invisible sobre el círculo para interactuar con él
boton_led = tk.Button(root, text="LED", width=10, height=5, command=toggle_rele)
boton_led.pack_forget()  # Ocultar el botón, ya que el círculo se utilizará para simular el LED

actualizar_etiqueta()  # Llamar a la función para empezar a mostrar los datos
root.mainloop()
ser.close()  # Cerrar el puerto serial al salir