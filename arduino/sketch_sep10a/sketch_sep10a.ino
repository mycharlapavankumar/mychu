#include <ESP8266WiFi.h>

#include <Wire.h>
int slot;
String A="https://api.thingspeak.com/update?api_key=XQNTZ6XBYE7RBIXZ&field1=";
String Z=" HTTP/1.1 \nHOST: api.thingspeak.com \r\n\r\n";
const char* ssid     = "searching..........."; // Your ssid
const char* password = "pavan182@"; // Your Password
 
char status;

WiFiServer server(80);
void setup() {
Serial.begin(115200);
delay(100);
Serial.print("Connecting to ");
Serial.println(ssid);
WiFi.begin(ssid, password);
 
while (WiFi.status() != WL_CONNECTED) {
delay(500);
Serial.print(".");
}
 
Serial.println("");
Serial.println("WiFi is connected");
server.begin();
Serial.println("Server started");
 
Serial.println(WiFi.localIP());

}
void loop (){
slot=50;
char slot_buff[16];
String slotx=dtostrf(slot,4,1,slot_buff);
String fslot=A+slotx+Z;
Serial.print("AT");
delay(2000);
Serial.print("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",80\r\n");
delay(3000);
String ciplength="AT+CIPSEND="+String(fslot.length())+"\r\n";
Serial.print(ciplength);
delay(3000);
Serial.print("AT+RST\r\n");
delay(3000);
 


  
}
