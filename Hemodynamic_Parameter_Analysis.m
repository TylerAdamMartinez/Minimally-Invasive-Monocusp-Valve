%%
% This code was created by Tyler Adam Martinez for the BMEN3310 Final
% Project. This MATlab script is for the Hemodynamic Parameter Analysis
% portion for the project.

%% This are the varibles and what they stand for.

%SVR // Systemic Vascular Resistance or Afterload on the heart
%MAP // Mean Arterial Pressure
%CVP // Central Venous Pressure
%CO  // Cardiac Output
%SV  // Stroke Volume
%HR  // Heart Rate
%SBP // Systomic Blood Pressure
%DBP // Diastolic Blood Pressure

%% 
SV = input('Enter in the Stroke Volume of the patient: ');
HR = input('Enter in the Heart Rate of the patient: ');
CO = SV * HR;
fprintf('The Cardiac Output of the patient is %u \n', CO);

SBP = input('Enter in the Systomic Blood Pressure of the patient: ');
DBP = input('Enter in the Diastolic Blood Pressure of the patient: ');
MAP = (((SBP) + (2 *(DBP)))/ 3);
fprintf('The Mean Arterial Pressure of the patient is %u \n', MAP);

CVP = input('Enter in the Central Venous Pressure of the patient: ');
SVR =  ((MAP - CVP)/(CO)) * 80;
fprintf('The Systemic Vascular Resistance of the patient is %d \n', CVR);
