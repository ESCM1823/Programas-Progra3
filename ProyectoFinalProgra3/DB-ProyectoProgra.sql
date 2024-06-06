CREATE DATABASE dbCamaraArduino

USE dbCamaraArduino

CREATE TABLE ArduinoInfo(
	id_usuario INT PRIMARY KEY NOT NULL IDENTITY(1,1),
	mensaje VARCHAR(250) NOT NULL,
)

INSERT INTO ArduinoInfo (mensaje) VALUES ('Hola test');
SELECT * FROM ArduinoInfo

SELECT @@SERVERNAME