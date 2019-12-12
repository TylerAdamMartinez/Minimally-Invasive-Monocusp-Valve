/*  This code was created by Tyler Adam Martinez for the BMEN3310 Final Project
 *  This code is for Arduino 1
 *  Arduino 1 controllers and powers the servo motor with magnet 
 *  The code for the hall sensor can be seen at https://github.com/TylerAdamMartinez/Minimally-Invasive-Monocusp-Valve
 */

#include <Servo.h>

Servo myservo;  // create servo object to control servo

unsigned int pos = 0;    // variable to store the servo position

void setup() 
{
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
 
  Serial.begin(9600);  //Serial Communication
}

void loop()
{
  // In our design the valve can't completely rotate to a perfect 90 degrees, so servo is set to only rotate to 85 degrees to count for this 
  for (pos = 0; pos <= 85; pos += 1)  
  { 
    myservo.write(pos);             
    Serial.println("Valve opening");
    delay(10);                       
  }

  for (pos = 85; pos >= 0; pos -= 1) 
  { 
    myservo.write(pos);
    Serial.println("Valve closing");
    delay(10);                       
  }

  //Heart is at rest, therefore, the valve should be stationary..  i.e. The servo should not move during this time
  delay(100);
}
