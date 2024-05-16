import cv2, serial
import tkinter as tk
from PIL import Image, ImageTk

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
ser = serial.Serial('COM4', 9600)

def send_command(command):
    ser.write(command.encode())
    print(f"Comando enviado: {command}")

def update_frame():
    _, img = cap.read()
    if not _:
        print("Error al leer la imagen de la cámara.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label.img = img  # Mantener una referencia al objeto PhotoImage
    label.config(image=img)
    label.after(10, update_frame)  # Actualizar la imagen cada 10 milisegundos

root = tk.Tk()
root.title("Reconocimiento Facial")

label = tk.Label(root)
label.pack(padx=10, pady=10)

update_frame() 

# Funciones para enviar comandos
button_1 = tk.Button(root, text="Abrir puerta", bg="green", command=lambda: send_command('1'))
button_1.pack(side=tk.TOP, padx=10, pady=10)

button_0 = tk.Button(root, text="Cerrar puerta", bg="red", command=lambda: send_command('0'))
button_0.pack(side=tk.TOP, padx=10, pady=10)

root.mainloop()

cap.release()
cv2.destroyAllWindows()