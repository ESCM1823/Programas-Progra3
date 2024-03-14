import time, serial

arduino = serial.Serial('COM4', 9600)
time.sleep(2)
arduino.write(b'0') #1 on 0 off
arduino.close()