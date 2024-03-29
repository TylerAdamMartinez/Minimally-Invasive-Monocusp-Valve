"""
This code was created by Tyler Adam Martinez for the BMEN3310 Final

#This are the varibles and what they stand for.

Hemodynamic Parameter Analysis
CS  // Cross-Sectional Area of the heart valve
vR  // Radius of Valve
DR  // Disk Radius 
TiA // Area of the Titanium wire
TiV // Volume of the Titanium wire
IRV // Inner Ring Volume
ORV // Outer Ring Volume
DR  // Disk Volume
NS  // Cost of Nitinol Stent per signal unit
PPC // Pure Pyrolytic Carbon per unit volume
Tf  // Teflon Fabric per unit volume
Ti  // Titanium Wire per unit volume

Hemodynamic Calculations
SVR // Systemic Vascular Resistance or Afterload on the heart
MAP // Mean Arterial Pressure
CVP // Central Venous Pressure
CO  // Cardiac Output
SV  // Stroke Volume
HR  // Heart Rate
SBP // Systomic Blood Pressure
DBP // Diastolic Blood Pressure
"""
import math
pi = 3.14159265359;

## Hemodynamic Parameter Analysis
CS = input("The cross-sectional area of the valve: ");
CS = int(CS);
vR = math.sqrt(CS/pi); #Convert CS to v radius 
height = 5.0; #mm
thinkness = 1.5; #mm
DR = vR - (2*thinkness); #calculating for the two outer disks
Diskheight = 1.5; #mm

#calculating the volumes of each material 
TiA = 0.1024 * pi; #.32mm is radius of Titanium wire, and .1024 is r^2
TiV = 2*vR *TiA; #mm^3
IRV = pi * pow((DR + thinkness), 2) - (pi * pow(DR, 2)) * height; #mm^3
ORV = pi * pow((DR + (2*thinkness)), 2) - pi * pow((DR + thinkness),2) * height; #mm^3
DV  = pi * pow(DR, 2) * Diskheight; #mm^3

#Constant Cost per volume values
NS  = 100; # $ per unit
PPC = 0.00052; # $ per 1 mm^3
TF  = 0.00014; # $ per 1 mm^3
Ti  = 0.00064; # $ per 1 mm^3

#Material Cost = Volume of Material * Cost per Unit Volume 
ORcost = ORV * TF + NS;
IRcost = IRV * PPC;
Dcost  = (DV*(.9)*PPC) + (DV*(.1)*TF) + TiV*Ti;
TotalCost = ORcost + IRcost + Dcost;

#Outputting result to user
print("The total cost of your heart valve is $",format(TotalCost,'.2f'));

## Hemodynamic Calculations
SV = input("Enter in the Stroke Volume of the patient: ");
SV = int(SV);
HR = input("Enter in the Heart Rate of the patient: ");
HR = int(HR);
CO = SV * HR;
print("The Cardiac Output of the patient is ",CO);

SBP = input("Enter in the Systomic Blood Pressure of the patient: ");
SBP = int(SBP);
DBP = input("Enter in the Diastolic Blood Pressure of the patient: ");
DBP = int(DBP);
MAP = (((SBP) + (2 *(DBP)))/ 3);
print("The Mean Arterial Pressure of the patient is ",format(MAP, '.3f'));

CVP = input("Enter in the Central Venous Pressure of the patient: ");
CVP = int(CVP);
SVR =  ((MAP - CVP)/(CO)) * 80;
print("The Systemic Vascular Resistance of the patient is ",format(SVR,'.3f'));
