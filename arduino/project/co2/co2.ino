const int slots=3;
const int enter=12;
void setup() {
  
int i;
  // put your setup code here, to run ouunj jb jmkmololp-pl09ki8jince:/*
  /*
pinMode(4,INPUT);
pinMode(5,INPUT);
pinMode(6,INPUT);*/
 pinMode(enter,INPUT);
 for(i=4;i<slots+3;i++)
  {
pinMode(i,INPUT);
}

Serial.begin(9600);
  
}

void loop() 
{
       
    int s[3],k=0,i,j,m;
  for(i=4;i<slots+4;i++)
  {
  s[i]=digitalRead(i);
  if(s[i]!=0)
    k++; 
  }
    delay(1000);
    Serial.print("empty slots=");
    Serial.println(k);
int enter1=digitalRead(enter);

 
 /*if(enter1==0 && s[0]!=0)
   {
     Serial.println(s[0]);
     slot_allot1 = 4;
     Serial.print("slot aloted is =");
     Serial.println(slot_allot1);
     
   } */
  if(m<5)
  {
    m=m+1;
    }
   else
   {
      m=0; 
   }  
 if(enter1==0)
  {  
    for(j=4;j<slots+4;j++)
      { 
      delay(1000);
         
      if(s[j]!=0)
       {
       //Serial.println("test111");
       int slot_allot=m+4;
       Serial.print("slot aloted is =");
       Serial.println(slot_allot);
       delay(1000);
      // int slot_allot1=slot_allot1+1;
        //m=slot_allot1;
        break;
      }
   }
   }
}
