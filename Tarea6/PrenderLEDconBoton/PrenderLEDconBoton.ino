/*const int grupo1 = 3, grupo2 = 4, grupo3 = 5, grupo4 = 6; //LEDs
const int boton1 = 8, boton2 = 9, boton3 = 10, boton4 = 11; //Botones
int estadoBoton1 = 0, estadoBoton2 = 0, estadoBoton3 = 0, estadoBoton4 = 0; // estado del boton

void setup() {
  //LEDs
  pinMode(grupo1, OUTPUT);
  pinMode(grupo2, OUTPUT);
  pinMode(grupo3, OUTPUT);
  pinMode(grupo4, OUTPUT);

  //Botones
  pinMode(boton1, INPUT);
  pinMode(boton2, INPUT);
  pinMode(boton3, INPUT);
  pinMode(boton4, INPUT);

  // Inicializar el monitor serial
  Serial.begin(9600);
}

void loop() {

  estadoBoton1 = digitalRead(boton1);
  estadoBoton2 = digitalRead(boton2);
  estadoBoton3 = digitalRead(boton3);
  estadoBoton4 = digitalRead(boton4);

  if (estadoBoton1 == HIGH){
    Serial.println("Boton 1 presionado");
    delay(100);
  }

  if (Serial.available() > 0) {
    char monitorSerial = Serial.read();

    if (monitorSerial == '1') {
      digitalWrite(grupo1, HIGH);
      Serial.println("Grupo 1 permitido encender");
    } else if (monitorSerial == '2') {
      digitalWrite(grupo2, HIGH);
      Serial.println("Grupo 2 permitido encender");
    } else if (monitorSerial == '3') {
      digitalWrite(grupo3, HIGH);
      Serial.println("Grupo 3 permitido encender");
    } else if (monitorSerial == '4') {
      digitalWrite(grupo4, HIGH);
      Serial.println("Grupo 4 permitido encender");
    } else if (monitorSerial == '5') {
      digitalWrite(grupo1, LOW);
      digitalWrite(grupo2, LOW);
      digitalWrite(grupo3, LOW);
      digitalWrite(grupo4, LOW);
      Serial.println("TODOS los grupos apagados");
    }
  }
}
*/

void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);

  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char estadoMonitor = Serial.read();
    if (estadoMonitor == 'A') {
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      Serial.println("Grupo Led A Encendidos");
    } else if (estadoMonitor == 'B') {
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      Serial.println("Grupo Led B Encendidos");
    } else if (estadoMonitor == 'C') {
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      Serial.println("Grupo Led C Encendidos");
    } else if (estadoMonitor == 'D') {
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      Serial.println("Grupo Led D Encendidos");
    } else if (estadoMonitor == 'E') {
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      Serial.println("TODAS las LEDs fueron Apagadas");
    }
  } else if (digitalRead(10) == LOW) {
    Serial.write('A');
    delay(100);
  } else if (digitalRead(11) == LOW) {
    Serial.write('B');
    delay(100);
  } else if (digitalRead(12) == LOW) {
    Serial.write('C');
    delay(100);
  } else if (digitalRead(13) == LOW) {
    Serial.write('D');
    delay(100);
  } 
}