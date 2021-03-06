#include "SparkFun_Si7021_Breakout_Library.h"
#include <Wire.h>
#define LIGHTSENSORPIN A1

float humidity = 0;
float tempf = 0;
float light_reading = 0;
float light_percent = 0;
float soil_moisture = 0;

//Create Instance of HTU21D or SI7021 temp and humidity sensor and MPL3115A2 barrometric sensor
Weather sensor;

int soilPin = A0; //Declare a variable for the soil moisture sensor 
int soilPower = 7; //Variable for Soil moisture Power

void setup()
{
    // Light set up
    pinMode(LIGHTSENSORPIN,  INPUT);

    // Temp/humidity setup
    Serial.begin(9600); // open serial over USB at 9600 baud
    //Initialize the I2C sensors and ping them
    sensor.begin();

    // Soil moisture setup
    pinMode(soilPower, OUTPUT); //Set D7 as an OUTPUT
    digitalWrite(soilPower, LOW); //Set to LOW so no power is flowing through the sensor
}

void getLight()
{
  light_reading = analogRead(LIGHTSENSORPIN); //Read light level
  light_percent = light_reading / 1023.0;      //Get percent of maximum value (1023)
  //square_ratio = pow(square_ratio, 2.0);      //Square to make response more obvious
}

void getSoilMoisture()
{
  digitalWrite(soilPower, HIGH);//turn D7 "On"
  delay(20);//wait 10 milliseconds 
  soil_moisture = analogRead(soilPin);//Read the SIG value form sensor 
  digitalWrite(soilPower, LOW);//turn D7 "Off"
}

void getWeather()
{
  // Measure Relative Humidity from the HTU21D or Si7021
  humidity = sensor.getRH();

  // Measure Temperature from the HTU21D or Si7021
  tempf = sensor.getTempF();
  // Temperature is measured every time RH is requested.
  // It is faster, therefore, to read it from previous RH
  // measurement with getTemp() instead with readTemp()
}

void printInfo()
{
  //This function prints the weather data out to the default Serial Port

  /*
  Serial.print("Temp:");
  Serial.print(tempf);
  Serial.print("F, ");

  Serial.print("Humidity:");
  Serial.print(humidity);
  Serial.println("%");

  Serial.print("Ambient Light:");
  Serial.println(light_reading);

  Serial.print("Light Percent:");
  Serial.println(light_percent);

  Serial.print("Soil Moisture:");
  Serial.println(soil_moisture);
  */

  Serial.print(tempf);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(light_reading);
  Serial.print(",");
  Serial.println(soil_moisture);
}

void loop()
{
  //Get readings from all sensors
  getWeather();
  getLight();
  getSoilMoisture();
  printInfo();
  delay(60000);
}
