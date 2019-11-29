
//This code was created by Tyler Adam Martinez for the BMEN3310 Finial Project
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
