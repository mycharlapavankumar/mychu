#include<LiquidCrystal.h>
#include <SoftwareSerial.h>
SoftwareSerial sc(0,1);
LiquidCrystal lcd(A5,A4,A0,A1,A2,A3);

const int slots=5;
const int enter1=8;

void setup() 
{
  
  sc.begin(9600);
  lcd.begin(16,2);
  int i;
 
  

 pinMode(enter1,INPUT);
 for(i=2;i<slots+2;i++)
  {
pinMode(i,INPUT);
}
for(i=9;i<slots+9;i++)
{
  pinMode(i,OUTPUT);
}


//Serial.begin(9600);
  
}

void loop() {
       
    int s[slots],k=0,i,j;
    int slot_alot,prealot=-1;
    while(1)
    {
      k=0;
  for(i=2;i<slots+2;i++)
  {
  s[i-2]=digitalRead(i);
  if(s[i-2]!=0)
  {
    k++;  
  }
  else
       digitalWrite(i+7,LOW);
 

}
if(sc.available()>0)
{   
 sc.write(k);
// Serial.println("data sent");
 //Serial.println(k);
 delay(5000);
}
    delay(1000);
    lcd.setCursor(0,0);
     // Serial.print("empty slots=");
      lcd.print("empty slots=");
 //Serial.println(k);
 lcd.print(k);
int enter=digitalRead(8);
int j1;
int alot_count=0;

 if(enter==0)
   {

    for(j=0;j<slots;j++)
      { 
      delay(1000);
    
      if(s[j]!=0)
       {
       
        if(prealot==j)
        {
        
          for(j=j+1;j<slots;j++)
          {
            if(s[j]!=0)
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
       //Serial.print("slot aloted is ");
       lcd.print("slot aloted is ");
       //Serial.println(slot_alot+1);
       lcd.print(slot_alot+1);
       delay(2000);
       digitalWrite(slot_alot+9,HIGH);
      break;
       }
    }
    lcd.clear();
    
   }
    }
   }
