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
 unsigned long myChannelNumber1 = 1010929 ;  
  unsigned long myChannelNumber2=  909371;
const char * myWriteAPIKey = "L27OMJABM46VH97B";
const char * myreadAPIKey1 = "RGD7DNDOEU2RR2CY";
const char * myWriteAPIKey2="XQNTZ6XBYE7RBIXZ";

void setup() 
{
  pinMode(D0,INPUT);
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
{      int x;
  long y=ThingSpeak.readIntField(myChannelNumber1,1,myreadAPIKey1);
  delay(2000);
  int pp=ThingSpeak.getLastReadStatus();
  //if(pp==200)
    if (s.available()>0)
  {
    s.write(y);
    data=s.read();
    Serial.println(data);
    
  }
  else
  Serial.println("no");
  if(digitalRead(D0)==LOW)
   x=ThingSpeak.writeField(myChannelNumber, 1,data, myWriteAPIKey);
else
   x=ThingSpeak.writeField(myChannelNumber2, 1,data, myWriteAPIKey2);
  Serial.println(x);

delay(2000);

}
