Valve = csvread('ValveSensor.csv');
ECG = csvread('ECG.csv');

subplot(2,1,1);
plot(ECG);
title("ECG"); ylabel("Amplitude (mV)"); xlabel("Time");
xlim([ 0 5000]);

subplot(2,1,2);
plot(Valve);
title("Signal from Valve Sensor"); ylabel("Amplitude (mV)"); xlabel("Time");
xlim([ 0 5000]);