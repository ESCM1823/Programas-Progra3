#include <Servo.h>

Servo servoMotor;// Crear un objeto de tipo Servo

int angulo = 0, cerrarPuerta = 3, abrirPuerta = 4;

void setup() {
  servoMotor.attach(2);// Conectar el servo al pin 2
  
  pinMode(abrirPuerta, OUTPUT);
  pinMode(cerrarPuerta, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  int numMonitorSerial = Serial.parseInt();

  if(numMonitorSerial == 1){
    // Mover el servo de 0 a 90 grados abrir puerta
    digitalWrite(abrirPuerta, HIGH);
    for (angulo = 0; angulo <= 95; angulo += 1) {
      servoMotor.write(angulo);  // Escribir el ángulo en el servo
      delay(15);  // Pequeña pausa para dar tiempo al servo de moverse
    }
    digitalWrite(abrirPuerta, LOW);
  }else if(numMonitorSerial == 0){
    // Mover el servo de 90 a 0 grados cerrar puerta
    digitalWrite(cerrarPuerta, HIGH);
    for (angulo = 95; angulo >= 0; angulo -= 1) {
      servoMotor.write(angulo);  // Escribir el ángulo en el servo
      delay(20);  // Pequeña pausa para dar tiempo al servo de moverse
    }
    digitalWrite(cerrarPuerta, LOW);
  }
}