#include<LiquidCrystal.h>
LiquidCrystal lcd(A5,A4,A0,A1,A2,A3);

void setup() {
  // put your setup code here, to run once:
lcd.begin(16, 2);
lcd.print("hi pavan");
}

void loop() {
  // put your main code here, to run repeatedly:
lcd.setCursor(0,1);
lcd.print("kumar");
}
