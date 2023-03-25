#include "Servo.h"

#define backPin 9 
#define rightPin 10
#define leftPin 11

const int stopWheel = 95;
//#define wspeed(s) s>0?stopWheel-s:stopWheel+s


Servo backservo; 
Servo leftservo;
Servo rightservo;
int wspeed(int s){
  if (s >0) {
    return stopWheel-s;
  }else {
    return stopWheel + s;
  }
}
void moveRight(){
  
}

void moveLeft(){
  
}
void moveBack(){
  leftservo.write(wspeed(-40));
  rightservo.write(wspeed(40));
}

void moveForward(){
  
}

void rotateRight(){
  leftservo.write(wspeed(40));
}

void rotateLeft(){
  
  rightservo.write(wspeed(40));
}

// a value of 95 writes 
void stopRightWheel(){
  rightservo.write(stopWheel);
}

void stopLeftWheel(){
  leftservo.write(stopWheel);
}

void moveWheels(int left, int right, int back){
  
}

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
//  pinMode(backPin, OUTPUT);
//  pinMode(rightPin, OUTPUT);
//  pinMode(leftPin, OUTPUT);
  backservo.attach(backPin);
  leftservo.attach(leftPin);
  rightservo.attach(rightPin);
  
  
}

void loop() {
  // put your main code here, to run repeatedly:
  rotateLeft();
  delay(1000);
    
  
  stopRightWheel();

  delay(1000);
    rotateRight();
  
  delay(1000);
  stopLeftWheel();

  delay(1000);
  moveBack();
  delay(1000);
  stopRightWheel();
  stopLeftWheel();
  delay(1000);
  
//  analogWrite(backPin, 255);
//  analogWrite(backPin, 255);
//  analogWrite(backPin, 255);
}
