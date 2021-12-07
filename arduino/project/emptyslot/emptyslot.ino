const int slots=3;
const int enter=12;
void setup() {
  int i;
  // put your setup code here, to run once:/*
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

void loop() {
       
    int s[3],k=0,i,j;
  for(i=4;i<slots+4;i++)
  {
  s[i]=digitalRead(i);
  if(s[i]!=0)
    k++;  
  // put your main code here, to run repeatedly:

}
    delay(1000);
      Serial.print("empty slots=");
 Serial.println(k);
int enter=digitalRead(12);
int slot_alot;
 if(enter==0)
   {

    for(j=4;j<slots+4;j++)
      { 
      delay(1000);
    
      if(s[j]!=0)
       {
        slot_alot=j;
       Serial.print("slot aloted is =");
       Serial.println(slot_alot);
      delay(1000);
      break;
    }
   }
   }
}
