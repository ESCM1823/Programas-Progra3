import serial
import time 

puerto = 'COM4'
velocidad = 9600
ser = serial.Serial(puerto,velocidad,timeout=1)
time.sleep(2)

ser.write(b'Hola arduino soy python')
time.sleep(1)
respuesta = ser.readline().decode('utf-8') 
print('Respuesta de Arduino:', respuesta)
ser.close()