import cv2, serial, time, threading
import tkinter as tk
from PIL import Image, ImageTk

# Configurar la comunicación serial
ser = serial.Serial('COM4', 9600)

# Función para leer datos del puerto serie
def serial_reader():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                handle_code(data)

def handle_code(code):
    try:
        digit = int(code)
        print("Código recibido:", digit)
    except ValueError:
        print("Mensaje desde Arduino:", code.strip())
        if code == 'Se abrio puerta':
            button_canvas.itemconfig(button_1, fill="green")
            button_canvas.itemconfig(button_0, fill="white")
        elif code == 'Se cerro puerta':
            button_canvas.itemconfig(button_0, fill="red")
            button_canvas.itemconfig(button_1, fill="white")

def send_command(command):
    ser.write(command.encode())
    print(f"Comando enviado: {command}")
    if command == '1':
        button_canvas.itemconfig(button_1, fill="green")
        button_canvas.itemconfig(button_0, fill="white")
    elif command == '0':
        button_canvas.itemconfig(button_0, fill="red")
        button_canvas.itemconfig(button_1, fill="white")

def update_frame():
    _, img = cap.read()
    if not _:
        print("Error al leer la imagen de la cámara.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        time.sleep(1.5)
        send_command('1')  # Enviar comando '1' si se detecta un rostro
    else:
        time.sleep(1.5)
        send_command('0')  # Enviar comando '0' si no se detecta ningún rostro

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(30, update_frame)

def abrir_puerta():
    send_command('1')

def cerrar_puerta():
    send_command('0')

# Cargar el clasificador de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capturar video de la cámara
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)

# Crear la ventana principal
root = tk.Tk()
root.title("Proyecto Final")

# Crear un marco principal
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Crear un canvas para la imagen de la cámara
canvas = tk.Canvas(main_frame, width=640, height=480)
canvas.pack()

# Crear un label para mostrar la imagen de la cámara
label = tk.Label(canvas)
label.pack()

# Crear otro canvas para los botones
button_canvas = tk.Canvas(main_frame, width=640, height=100, bg='white')
button_canvas.pack()

# Crear botones circulares en el canvas de botones
button_1 = button_canvas.create_oval(70, 20, 130, 80, outline="black", fill="white")
button_0 = button_canvas.create_oval(510, 20, 570, 80, outline="black", fill="white")

# Crear y ejecutar el hilo para leer datos del puerto serie
serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

# Iniciar la actualización de frames
update_frame()

# Iniciar el bucle principal de Tkinter
root.mainloop()

# Liberar la captura de video
cap.release()