import cv2, serial, time, threading
import tkinter as tk
from PIL import Image, ImageTk

# Clase para manejar la comunicación serial
class SerialHandler:
    def __init__(self, port):
        self.ser = serial.Serial(port, 9600)

    # Leer datos del puerto serie en un bucle
    def read_serial(self, handle_code):
        while True:
            if self.ser.in_waiting > 0:
                data = self.ser.readline().decode().strip()
                if data:
                    handle_code(data)

    # Enviar comandos al puerto serie
    def send_command(self, command):
        self.ser.write(command.encode())
        print(f"Comando enviado: {command}")

# Clase para manejar la cámara
class CameraHandler:
    def __init__(self, cascade_path):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 30)

    # Obtener un frame de la cámara
    def get_frame(self):
        ret, img = self.cap.read()
        if not ret:
            print("Error al leer la imagen de la cámara.")
            return None
        return img

    # Liberar la cámara
    def release(self):
        self.cap.release()

# Clase principal de la aplicación
class App:
    def __init__(self, root, serial_port, cascade_path):
        self.root = root
        self.serial_handler = SerialHandler(serial_port)
        self.camera_handler = CameraHandler(cascade_path)

        self.root.title("Proyecto Final")
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame, width=640, height=480)
        self.canvas.pack()
        self.label = tk.Label(self.canvas)
        self.label.pack()

        self.button_canvas = tk.Canvas(self.main_frame, width=640, height=100, bg='white')
        self.button_canvas.pack()
        self.button_1 = self.button_canvas.create_oval(70, 20, 130, 80, outline="black", fill="white")
        self.button_0 = self.button_canvas.create_oval(510, 20, 570, 80, outline="black", fill="white")

        # Iniciar hilo para leer datos del puerto serie
        self.serial_thread = threading.Thread(target=self.serial_handler.read_serial, args=(self.handle_code,))
        self.serial_thread.daemon = True
        self.serial_thread.start()

        # Iniciar la actualización de frames
        self.update_frame()

    # Manejar los códigos recibidos del puerto serie
    def handle_code(self, code):
        try:
            digit = int(code)
            print("Código recibido:", digit)
        except ValueError:
            print("Mensaje desde Arduino:", code.strip())
            if code == 'Se abrio puerta':
                self.button_canvas.itemconfig(self.button_1, fill="green")
                self.button_canvas.itemconfig(self.button_0, fill="white")
            elif code == 'Se cerro puerta':
                self.button_canvas.itemconfig(self.button_0, fill="red")
                self.button_canvas.itemconfig(self.button_1, fill="white")

    # Enviar comandos al Arduino y actualizar los botones
    def send_command(self, command):
        self.serial_handler.send_command(command)
        if command == '1':
            self.button_canvas.itemconfig(self.button_1, fill="green")
            self.button_canvas.itemconfig(self.button_0, fill="white")
        elif command == '0':
            self.button_canvas.itemconfig(self.button_0, fill="red")
            self.button_canvas.itemconfig(self.button_1, fill="white")

    # Actualizar el frame de la cámara y detectar rostros
    def update_frame(self):
        img = self.camera_handler.get_frame()
        if img is None:
            return

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.camera_handler.face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            time.sleep(1.5)
            self.send_command('1')
        else:
            time.sleep(1.5)
            self.send_command('0')

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        self.label.after(30, self.update_frame)

    # Métodos para abrir y cerrar la puerta
    def abrir_puerta(self):
        self.send_command('1')

    def cerrar_puerta(self):
        self.send_command('0')

    # Liberar recursos al cerrar la aplicación
    def on_closing(self):
        self.camera_handler.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, 'COM4', 'haarcascade_frontalface_default.xml')
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
