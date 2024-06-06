import cv2, serial, time, threading
import tkinter as tk
from PIL import Image, ImageTk
import sys
import pypyodbc as odbc

class DatabaseHandler:
    def __init__(self, driver_name, server_name, database_name):
        self.connection_string = f"""
            DRIVER={{{driver_name}}};
            SERVER={{{server_name}}};
            DATABASE={{{database_name}}};
            Trust_Connection=yes;
        """
        self.connect()

    def connect(self):
        try:
            self.db = odbc.connect(self.connection_string)
        except Exception as e:
            print(e)
            sys.exit()
        else:
            self.cursor = self.db.cursor()

    def insert_message(self, message):
        insert_statement = """
            INSERT INTO ArduinoInfo
            VALUES (?);
        """
        try:
            self.cursor.execute(insert_statement, [message])
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f"Error al insertar en la base de datos: {e}")

    def close(self):
        if self.db.connected == 1:
            self.cursor.close()
            self.db.close()
            print("Conexión a la base de datos cerrada")

class SerialReader:
    def __init__(self, port, baudrate, gui, db_handler):
        self.ser = serial.Serial(port, baudrate)
        self.gui = gui
        self.db_handler = db_handler

    def read_serial(self):
        while True:
            if self.ser.in_waiting > 0:
                data = self.ser.readline().decode().strip()
                if data:
                    self.handle_code(data)

    def handle_code(self, code):
        try:
            digit = int(code)
            print("Código recibido:", digit)
        except ValueError:
            print("Mensaje desde Arduino:", code.strip())
            self.db_handler.insert_message(code)
            self.gui.update_buttons(code)

    def send_command(self, command):
        self.ser.write(command.encode())
        print(f"Comando enviado: {command}")
        self.gui.update_buttons(command)

class CameraHandler:
    def __init__(self, cascade_path, gui, serial_reader):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.gui = gui
        self.serial_reader = serial_reader

    def update_frame(self):
        _, img = self.cap.read()
        if not _:
            print("Error al leer la imagen de la cámara.")
            return

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            time.sleep(2)
            self.serial_reader.send_command('1')
        else:
            time.sleep(2)
            self.serial_reader.send_command('0')

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.gui.update_image(imgtk)
        self.gui.schedule_update(self.update_frame)

    def release(self):
        self.cap.release()
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Proyecto Final")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame, width=640, height=480)
        self.canvas.pack()

        self.label = tk.Label(self.canvas)
        self.label.pack()

        self.button_canvas = tk.Canvas(self.main_frame, width=640, height=100, bg='white')
        self.button_canvas.pack()

        self.button_1 = self.button_canvas.create_oval(70, 20, 130, 80, outline="black", fill="white")
        self.button_0 = self.button_canvas.create_oval(510, 20, 570, 80, outline="black", fill="white")

    def update_buttons(self, code):
        if code == 'Se abrio puerta' or code == '1':
            self.button_canvas.itemconfig(self.button_1, fill="green")
            self.button_canvas.itemconfig(self.button_0, fill="white")
        elif code == 'Se cerro puerta' or code == '0':
            self.button_canvas.itemconfig(self.button_0, fill="red")
            self.button_canvas.itemconfig(self.button_1, fill="white")

    def update_image(self, imgtk):
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

    def schedule_update(self, func):
        self.label.after(30, func)

    def start(self):
        self.root.mainloop()

def main():
    db_handler = DatabaseHandler('SQL Server', 'ESCM-PC\SQLEXPRESS', 'dbCamaraArduino')
    gui = GUI()
    serial_reader = SerialReader('COM4', 9600, gui, db_handler)
    camera_handler = CameraHandler('haarcascade_frontalface_default.xml', gui, serial_reader)

    serial_thread = threading.Thread(target=serial_reader.read_serial)
    serial_thread.daemon = True
    serial_thread.start()

    gui.schedule_update(camera_handler.update_frame)
    gui.start()

    camera_handler.release()
    db_handler.close()

if __name__ == "__main__":
    main()