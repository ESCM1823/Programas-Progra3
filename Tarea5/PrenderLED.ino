char dato;

void setup() {
  pinMode(3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0){
    dato = Serial.read();
    if(dato == '1'){
      digitalWrite(3, HIGH);
    }
    if(dato == '0'){
      digitalWrite(3, LOW);
    }
  }
}