  const int slots=3;
  int s[slots];
  const int in_s=12,out_s=13;
  
void setup() {
int i;
Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(in_s,INPUT);
  pinMode(out_s,INPUT);
  for(i=4;i<slots+3;i++)
  {
pinMode(i,INPUT);
}
}

void loop() {
  int slots=3;
  int s[3];
  int i,k=0,k1;
  int slot_alot;
  for(i=4;i<slots+3;i++);
  {
  s[i]=digitalRead(i);
  if(s[i]!=0)
    k++;
  }
  Serial.print("empty=");
  Serial.println(k);
  /*int enter=digitalRead(in_s);
  if(enter==0)
   {
    for(i=0;i<slots;i++)
    {
      if(s[i]==0)
       {slot_alot=i+1;
       Serial.print("slot aloted is =");
       Serial.print(slot_alot);
    }
   }
   }
}*/
}
  
  
  // put your main code here, to run repeatedly:
