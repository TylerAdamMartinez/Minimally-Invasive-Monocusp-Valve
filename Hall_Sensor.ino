/*  This code was created by Tyler Adam Martinez for the BMEN3310 Final Project
 *  This code is for Arduino 2
 *  Arduino 2 powers the hall sensor a determines if signal HIGH or LOW digitally 
 *  The hall sensor signal captured by an oscilloscope can be seen on the final Report posted in https://github.com/TylerAdamMartinez/Minimally-Invasive-Monocusp-Valve
 */
 
int Hall_Vcc = 8;
int Hall_Signal = 9;
int Valve = 0;

void setup()
{
  pinMode(Hall_Vcc, OUTPUT);
  pinMode(Hall_Signal, INPUT);
  Serial.begin(9600);
}

void loop() 
{
  //Setting the Vcc to 5V(HIGH) && creating the declaring the varible for the branch to compare too. 
  digitalWrite(Hall_Vcc, HIGH);
  Valve = digitalRead(Hall_Signal);
  
  //Determining if the Valve is closed or open.
  if(Valve == HIGH)
  {
    Serial.println("The Valve is Open");
  }
  else
  {
    Serial.println("The Valve is Closed");
  }

  //This will delay the another loop iteration for half a second to make it not as fast. 
  delay(500);

}
