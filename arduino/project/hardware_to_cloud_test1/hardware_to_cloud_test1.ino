 #include <ESP8266WiFi.h>
 #include <ThingSpeak.h>
#include <WiFiClient.h>
#include <SoftwareSerial.h>
SoftwareSerial s(D6,D5);
String data;
const char *ssid =  "soni";    
const char *pass =  "soni1234";

WiFiClient client;
 unsigned long myChannelNumber = 948514 ; 
 
const char * myWriteAPIKey = "L27OMJABM46VH97B";

void setup() 
{
 s.begin(9600);
       Serial.begin(9600);
       delay(10); 
               
       Serial.println("Connecting to ");
       Serial.println(ssid); 
    
       WiFi.begin(ssid, pass); 
       ThingSpeak.begin(client);
       while (WiFi.status() != WL_CONNECTED) 
          {
            delay(500);
            Serial.print(".");
          }
      Serial.println("");
      Serial.println("WiFi connected"); 
}
 
void loop() 
{      
 s.write("s");
  if (s.available()>0)
  {
    data=s.read();
    Serial.println(data);
  }
int x=ThingSpeak.writeField(myChannelNumber, 1,data, myWriteAPIKey);
Serial.println(x);
delay(2000);

}
