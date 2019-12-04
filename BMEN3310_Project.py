import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def main():
    valve = pd.read_csv('ValveSensor.csv'); 
    ECG = pd.read_csv('ECG.csv');           
        
    #plotting the data to the figure
    plt.subplot(2, 1, 1);
    plt.plot(ECG);
    plt.title("ECG"); plt.ylabel("Amplitude (mV)"); plt.xlabel("Time");
    plt.xlim(0, 5000);
    
    plt.subplot(2, 1, 2);
    plt.plot(valve);
    plt.title("Signal from Valve Sensor"); plt.ylabel("Amplitude (mV)"); plt.xlabel("Time");
    plt.xlim(0, 5000);
    plt.show(); 

if __name__ == "__main__":
    main()
    