import serial, time, tkinter

arduino = serial.Serial('COM4', 9600)

#Hacer que el usuario ingrese el numero 
while True:

    ingresoNum = input("Ingrese el valor que desea enviar al arduino (ingresar 's o S' para salir): ")

    #usa metodos para salir del programa
    if ingresoNum.lower() == 's':
        print("Saliendo del programa...")
        break

    #esto sirve para que el usuario ingrese el caracter
    arduino.write(str.encode(ingresoNum))

    print("Valor enviado correctamente ;)")

arduino.close()#cerrar el serial