#include<LiquidCrystal.h>
#include <SoftwareSerial.h>
SoftwareSerial sc(0,1);
LiquidCrystal lcd(A5,A4,A0,A1,A2,A3);

const int slots=5;
const int enter1=8;
int bk[slots];
int inbook(int x)
{
  int i;
  for(i=0;i<slots;i++)
  {
    if(bk[i]==x)
     return 0;
  }
  return 1;
  
}
int stor()
{
  int i;
  for(i=0;i<slots;i++)
  {
    if(bk[i]==-1)
     return i;
  }
  return -1;
}
int bookcount()
{
  int i,j=0;
  for(i=0;i<slots;i++)
   if(bk[i]!=-1)
     j++;

     return j;
  
}
int come(int x)
{
  int i;
  for(i=0;i<slots;i++)
  {
    if(bk[i]==x)
     bk[i]=-1;
  }
}
void setup() 
{
  
  sc.begin(9600);
  lcd.begin(16,2);
  int i;
 
  
pinMode(7,OUTPUT);
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
 for(i=0;i<slots;i++)
  {
    if(bk[i]=-1)
     return i;
  }
  
}
void loop() {
       
    int s[slots],k=0,i,j;
    int slot_alot,prealot=-1;
    int book=0,bb=0,x;
    
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
  {
       digitalWrite(i+7,LOW);
       come(i-2);
 
  }
}
if(sc.available()>0)
{   
 book=sc.read();
 delay(2000);
 if(book==0)
 {
  digitalWrite(7,LOW);
  
 sc.write(k-bookcount());
 
// Serial.println("data sent");
 //Serial.println(k);
 delay(5000);
}
else
{
     for(j=0;j<slots;j++)
     {
      if(s[j]!=0)
       {
        x=inbook(j);
        if(x==1)
        {
          digitalWrite(7,HIGH);
          delay(1000);
        bk[stor()]=j;
        sc.write(j);
        }
        
        
       }
     }
     
  
}
}

    delay(1000);
    lcd.setCursor(0,0);
     // Serial.print("empty slots=");
      lcd.print("empty slots=");
 //Serial.println(k);
 lcd.print(k-bookcount());
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
