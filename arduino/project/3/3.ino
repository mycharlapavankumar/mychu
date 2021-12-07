const int slots=3;
void setup() {
  int i;
  // put your setup code here, to run once:/*
  /*
pinMode(4,INPUT);
pinMode(5,INPUT);
pinMode(6,INPUT);*/
 for(i=4;i<slots+3;i++)
  {
pinMode(i,INPUT);
}
pinMode(12,INPUT);
Serial.begin(9600);

}

void loop() {
  int s[3],k=0,i;
  for(i=4;i<7;i++)
  {
  s[i]=digitalRead(i);
  if(s[i]!=0)
    k++;
     
 
  
 
  // put your main code here, to run repeatedly:

}
 delay(1000);
      Serial.print("empty slots=");
 Serial.println(k);
}
