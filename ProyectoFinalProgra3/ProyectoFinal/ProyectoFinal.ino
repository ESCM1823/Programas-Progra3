#include <Servo.h>

Servo servoMotor;  // Crear un objeto de tipo Servo

int angulo = 0, cerrarPuerta = 3, abrirPuerta = 4;

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
      for (angulo = 0; angulo <= 90; angulo += 1) {
        servoMotor.write(angulo);  // Escribir el ángulo en el servo
        delay(20);  // Pequeña pausa para dar tiempo al servo de moverse
      }
      digitalWrite(abrirPuerta, LOW);
    } else if (numMonitorSerial == '0') {
      Serial.println("Se cerro puerta");
      digitalWrite(cerrarPuerta, HIGH);
      for (angulo = 90; angulo >= 0; angulo -= 1) {
        servoMotor.write(angulo);  // Escribir el ángulo en el servo
        delay(20);  // Pequeña pausa para dar tiempo al servo de moverse
      }
      digitalWrite(cerrarPuerta, LOW);
    }
  }
}