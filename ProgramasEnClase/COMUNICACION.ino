void setup() {
  pinMode(1, OUTPUT);
  Serial.begin(9600);
}

char datoPython = Serial.read();

void loop() {
  digitalWrite(1, HIGH);
  delay(1000);
  Serial.println("Hola, desde arduino");
  digitalWrite(1, LOW);
  delay(1000);
  Serial.print(datoPython);
}
