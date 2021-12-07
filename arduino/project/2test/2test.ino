void setup() {
  // put your setup code here, to run once:
 pinMode(5,INPUT);
 Serial.begin(9600);
}

void loop() {
  int k=digitalRead(6);
  if(k==0)
  {
    delay(1000);
  Serial.println("pavan");
  }
  else
  {
        delay(1000);
  Serial.println("no");
  
  }
  
  // put your main code here, to run repeatedly:

}
