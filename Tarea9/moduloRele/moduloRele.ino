int rele = 2;

void setup() {
  pinMode(rele, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  Serial.println("Rele ON");
  digitalWrite(rele, HIGH);
  delay(2000);
  Serial.println("Rele OFF");
  digitalWrite(rele, LOW);
  delay(2000);
}
