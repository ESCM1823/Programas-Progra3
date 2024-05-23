#include <Servo.h>

Servo servoMotor;  // Crear un objeto de tipo Servo

int anguloAbierto = 90, anguloCerrado = 0, cerrarPuerta = 3, abrirPuerta = 4;

void setup() {
  servoMotor.attach(2);  // Conectar el servo al pin 2

  pinMode(abrirPuerta, OUTPUT);
  pinMode(cerrarPuerta, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char numMonitorSerial = Serial.read();

    if (numMonitorSerial == '1') {
      Serial.println("Se abrio puerta");
      digitalWrite(abrirPuerta, HIGH);
      delay(1000);
      servoMotor.write(anguloAbierto);  // Escribir el ángulo en el servo
      delay(500);
      digitalWrite(abrirPuerta, LOW);
    } else if (numMonitorSerial == '0') {
      Serial.println("Se cerro puerta");
      digitalWrite(cerrarPuerta, HIGH);
      delay(1000);
      servoMotor.write(anguloCerrado);  // Escribir el ángulo en el servo
      delay(500);
      digitalWrite(cerrarPuerta, LOW);
    }
  }
}