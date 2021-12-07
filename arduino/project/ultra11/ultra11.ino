#include <LiquidCrystal.h>
#include<SoftwareSerial.h>
SoftwareSerial sc(0,1);
const int slots=2;
long dur;
int dis[slots];
const int rs = A0 , en = A1, d4 = A2, d5 = A3, d6 = A4, d7 = A5;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  lcd.begin(16, 2);
 sc.begin(9600);
 // Serial.begin(9600);
 
pinMode(7,OUTPUT);//trigpin
for(int i=2;i<slots+2;i++)
pinMode(i,INPUT);
pinMode(8,INPUT);//enters
Serial.print("hello");


}

void loop() {
  // put your main code here, to run repeatedly:
int k=0,i,prealot=-1,j,slot_alot;
while(1)
{
  k=0;
for(i=2;i<slots+2;i++)
{
digitalWrite(7,LOW);
delayMicroseconds(20);
digitalWrite(7,HIGH);
delayMicroseconds(100);
digitalWrite(7,LOW);
dur=pulseIn(i,HIGH);
dis[i-2]=dur*0.034/2;
}
for(i=0;i<slots;i++)
{
  if(!((dis[i]<=100)&&(dis[i]>=20)))
  {
    k++;
  
  }
//Serial.print("distnce:");
//Serial.print(i);
//Serial.println(dis[i]);

}
delay(2000);
//Serial.println(k);
lcd.clear();
lcd.print("empty slots=");
lcd.print(k);
 Serial.println(k);
if(sc.available()>0)
{
 // Serial.print("serial");
  //Serial.println(k);
 sc.write(k); 
 delay(2000);
}
digitalWrite(7,LOW);
delayMicroseconds(20);
digitalWrite(7,HIGH);
delayMicroseconds(100);
digitalWrite(7,LOW);
int enter=digitalRead(8);
dur=pulseIn(8,HIGH);
int dist=dur*0.034/2;
Serial.print("dit:");
Serial.println(dist);
if((dist<=100)&&(dist>=20))
{
 // Serial.println("enter");
  for(j=0;j<slots;j++)
{
  if(!((dis[j]<=100)&&(dis[j]>=20)))
  {
    if(prealot==j)
    { 
      for(j=j+1;j<slots;j++)
      { 
        if(!((dis[j]<=100)&&(dis[j]>=20)))
        {
          prealot=j;
          slot_alot=j;
          break;
        }
      }
    }
    else
    {
      slot_alot=j;
      prealot=j;
        }
        lcd.setCursor(0,1);
        //Serial.print("slot aloted is");
        lcd.print("slot aloted is");
       // Serial.println(slot_alot+1);
        lcd.print(slot_alot+1);
        delay(2000);
        break;
        
      }
    }
  lcd.clear();
  }
}
}
