int grupo1 = 3;
int grupo2 = 4;
int grupo3 = 5;
int grupo4 = 6;

void setup() {
  pinMode(grupo1, OUTPUT);
  pinMode(grupo2, OUTPUT);
  pinMode(grupo3, OUTPUT);
  pinMode(grupo4, OUTPUT);
  Serial.begin(9600);
}

void loop() {

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