import serial
import tkinter as tk

ser = serial.Serial('COM4', 9600)

root = tk.Tk()
root.title("Lab 10")
root.configure(bg='darkblue')

ancho_ventana = 250
alto_ventana = 250
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2
root.geometry(f'{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}')

mensaje_label = tk.Label(root, text="", bg='darkblue', fg='white')
mensaje_label.pack()

frame_botones = tk.Frame(root)
frame_botones.pack(expand=True)
frame_botones.configure(bg='darkblue')

def enviar_comando(comando):
    ser.write(comando.encode())

def boton_presionado(comando):
    enviar_comando(comando)

botonStepper = tk.Button(frame_botones, text="Iniciar Stepper", command=lambda: boton_presionado('1'))
botonStepper.pack(side=tk.LEFT, padx=5, pady=5)
botonStepper.configure(bg='white')

botonServo = tk.Button(frame_botones, text="Iniciar Servo", command=lambda: boton_presionado('2'))
botonServo.pack(side=tk.LEFT, padx=5, pady=5)
botonServo.configure(bg='white')

root.mainloop()