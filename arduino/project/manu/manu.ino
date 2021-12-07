#include <LiquidCrystal.h>
#include <Servo.h>
const int coin = 2;
boolean insert = false;
volatile int pulse = 0;
Servo myservo;
int pos = 0;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


int cout=100;


void setup() {
    myservo.attach(9); 
  lcd.begin(16, 2);
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(2), coinInterrupt, RISING);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.setCursor(0, 1);
  lcd.print("remaing");
  lcd.print(count);
  if (insert) {
    insert = false;
    Serial.println("coin detected!");
    lcd.print("take the product");
    count=count-1;
    delay(1000);
      myservo.write(180);              // tell servo to go to position in variable 'pos'
    delay(1000);  
      myservo.write(0);    
  }
}

//interrupt
void coinInterrupt() {
  pulse++ ;
  insert = true;
}
