#include <SoftwareSerial.h>
SoftwareSerial s(5,6);
 
void setup() {
s.begin(9600);
}
 
void loop() {
int data=50;
if(s.available()>0)
{
  Serial.println("work");
 s.write(data);
}
}
