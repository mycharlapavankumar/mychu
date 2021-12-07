 #include <ESP8266WiFi.h>
 #include <ThingSpeak.h>
#include <WiFiClient.h>
const char *ssid =  "searching...........";     // replace with your wifi ssid and wpa2 key
const char *pass =  "pavan182@";

WiFiClient client;
 unsigned long myChannelNumber = 915331 ; 
 
const char * myWriteAPIKey = "3H3S6IF426HLGR83";
  int val=1000;
void setup() 
{
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


  
  delay(100);
  if(val<100)
    val=val*2;
  else 
   val=val/2;
   Serial.println(val); 
 
ThingSpeak.writeField(myChannelNumber, 1,val, myWriteAPIKey);
}
