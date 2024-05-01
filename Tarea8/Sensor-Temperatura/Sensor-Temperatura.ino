#include <DHT.h>//libreria

#define DHTTYPE DHT11 //especificar el tipo de sensor
#define DHTPIN 2 //PIN de datos del sensor

DHT sensor(DHTPIN, DHTTYPE);

void setup(){
  Serial.begin(9600);
  sensor.begin();
}

void loop(){
  delay(2000);

  float hum = sensor.readHumidity();
  float temp = sensor.readTemperature();

  Serial.print("Humedad: ");
  Serial.print(hum);
  Serial.print("%     ");
  Serial.print("Temperatura: ");
  Serial.print(temp);
  Serial.print("°C");
  Serial.print("\n");
}