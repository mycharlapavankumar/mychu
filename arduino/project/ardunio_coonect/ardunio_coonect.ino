//Arduino code
#include <SoftwareSerial.h>
SoftwareSerial s(0,1);
 
void setup() {
s.begin(9600);
}
 
void loop() {
int i;

if(s.available()>0)
{
  for (i=90;i<150;i++)
  {
 s.write(i);
 delay(10000);
  }
}

}
