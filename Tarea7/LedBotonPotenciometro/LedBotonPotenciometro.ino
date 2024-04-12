//Variables
int ledVerde = 2, ledAmarillo = 4, ledRojo = 6; //LEDs
int preOrden = 8, inOrden = 10, postOrden = 12; //botones
bool leerPoten = true;

void setup() {
  //LEDs
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  pinMode(ledRojo, OUTPUT);

  //Botones
  pinMode(preOrden, INPUT_PULLUP);
  pinMode(inOrden, INPUT_PULLUP);
  pinMode(postOrden, INPUT_PULLUP);

  Serial.begin(9600);
}

void loop() {
  // Leer potenciómetro
  if(leerPoten){
    int poten = analogRead(A0);
    Serial.println(poten);
    delay(5);
  }

  //Leer el estado de los botones
  int estadoPreOrden = digitalRead(preOrden);
  int estadoInOrden = digitalRead(inOrden);
  int estadoPostOrden = digitalRead(postOrden);

  //LEDs ON cuando el estado del boton sea LOW
  if (estadoPreOrden == LOW) {
    // Pre-orden
    Serial.println("PreOrden ON");
    digitalWrite(ledAmarillo, HIGH);
    Serial.println(4);
    delay(500);
    digitalWrite(ledAmarillo, LOW);
    Serial.println(0);
    delay(500);
    digitalWrite(ledVerde, HIGH);
    Serial.println(2);
    delay(500);
    digitalWrite(ledVerde, LOW);
    Serial.println(0);
    delay(500);
    digitalWrite(ledRojo, HIGH);
    Serial.println(6);
    delay(500);
    digitalWrite(ledRojo, LOW);
    Serial.println(0);
    delay(500);
    Serial.println("PreOrden OFF");
    delay(1000);
  }

  if (estadoInOrden == LOW) {
    // In-orden
    Serial.println("InOrden ON");
    digitalWrite(ledVerde, HIGH);
    Serial.println(2);
    delay(500);
    digitalWrite(ledVerde, LOW);
    Serial.println(0);
    delay(500);
    digitalWrite(ledAmarillo, HIGH);
    Serial.println(4);
    delay(500);
    digitalWrite(ledAmarillo, LOW);
    Serial.println(0);
    delay(500);
    digitalWrite(ledRojo, HIGH);
    Serial.println(6);
    delay(500);
    digitalWrite(ledRojo, LOW);
    Serial.println(0);
    delay(500);
    Serial.println("InOrden OFF");
    delay(1000);
  }

  if (estadoPostOrden == LOW) {
    // Post-orden
    Serial.println("PostOrden ON");
    digitalWrite(ledVerde, HIGH);
    Serial.println(2);
    delay(500);
    digitalWrite(ledVerde, LOW);
    Serial.println(0);
    delay(500);
    digitalWrite(ledRojo, HIGH);
    Serial.println(6);
    delay(500);
    digitalWrite(ledRojo, LOW);
    Serial.println(0);
    delay(500);
    digitalWrite(ledAmarillo, HIGH);
    Serial.println(4);
    delay(500);
    digitalWrite(ledAmarillo, LOW);
    Serial.println(0);
    delay(500);
    Serial.println("PostOrden OFF");
    delay(1000);
  }

}