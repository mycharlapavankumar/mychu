#include<LiquidCrystal.h>
const int rs=2, en=3, d4=4,d5=5, d6=6,d7=7;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);
void setup() {
  Serial.begin(9600);
  pinMode(A5,INPUT);
  pinMode(13,OUTPUT);
  pinMode(8,OUTPUT);
  lcd.begin(16,2);
}

void loop() {
  float sensor_volt;
  float sensorValue;
  sensorValue=analogRead(A5);
  sensor_volt=sensorValue/1024*5;
  Serial.print("sensor_volt=");
  Serial.print(sensor_volt);
  Serial.println("V");
  if(sensor_volt>3.0)
  {
    lcd.setCursor(0,0);
    lcd.clear();
    lcd.print("ignition off");
    digitalWrite(13,HIGH);
    digitalWrite(8,HIGH);
    delay(1000);
  }
  else{
    lcd.setCursor(0,0);
    lcd.clear();
    lcd.print("ignition on");
    digitalWrite(13,LOW);
    digitalWrite(8,LOW);
  }
  }
  // put your main code here, to run repeatedly:
//akshayakilli8@gmail.com
