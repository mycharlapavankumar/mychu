#include <SoftwareSerial.h>
SoftwareSerial s(D6,D5);
int data;
 
void setup() {
  // Initialize Serial port
  Serial.begin(9600);
  s.begin(9600);
}
 
void loop() 
{      
 s.write("s");
   Serial.println(data);
  if (s.available()>0)
  {
    data=s.read();
    Serial.println(data);
  }
}
