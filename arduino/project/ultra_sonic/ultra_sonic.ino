int trigPin = D1;      // trig pin of HC-SR04
int echoPin = D2;     // Echo pin of HC-SR

long duration, distance;

void setup() {
  
Serial.begin(9600);

  pinMode(D3,OUTPUT);
  pinMode(D7,OUTPUT);
  pinMode(trigPin, OUTPUT);         // set trig pin as output
  pinMode(echoPin, INPUT);          //set echo pin as input to capture reflected waves
}

void loop() {

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);   
  digitalWrite(trigPin, HIGH);     // send waves for 10 us
  delayMicroseconds(10);
  duration = pulseIn(echoPin, HIGH); // receive reflected waves
  distance = duration*0.034/2;;   // convert to distance
  delay(10);
    // If you dont get proper movements of your robot then alter the pin numbers
 Serial.println(distance);
 
 if(distance<20)
 {
  digitalWrite(D3,HIGH);
  digitalWrite(D7,HIGH);
  
 }
 /*else{
  digitalWrite(D3,LOW);
  digitalWrite(D3,LOW);
 }*/
  
 else if((distance>20)&&(distance<50))
 {
  analogWrite(D3,512);
  digitalWrite(D7,LOW);
 }
 else
 {
  digitalWrite(D3,LOW);
  digitalWrite(D7,LOW);
 }
   
}
