import numpy as np
import scipy.io.wavfile as wav
import audioInput
import testSetInput
import matplotlib.pyplot as plt
import numpyFFT
import sounddevice as sd

#define linear transition function
def linearTransition():
    '''
    first thoughts with just gain from 0.

    while True:
        #get user input for slope, centre frequency, gain
        slope = float(input("Enter the slope (non-zero): "))
        gain = float(input("Enter the gain: "))
        centreFreq = float(input("Enter the centre frequency: "))

        #find edge frequencies
        edgeFreq1 = centreFreq - gain/(2*slope)
        edgeFreq2 = centreFreq + gain/(2*slope)

        #define functrion
        linearFunction = np.zeros(len(numpyFFT.fourier))
        for i in range(len(numpyFFT.plotAxis)):
            if numpyFFT.plotAxis[i] < edgeFreq1:
                linearFunction[i] = 0
            elif edgeFreq1 <= numpyFFT.plotAxis[i] <= edgeFreq2:
                linearFunction[i] = slope * (numpyFFT.plotAxis[i] - edgeFreq1)
            else:
                linearFunction[i] = gain
        stop = input("Do you want to stop? (y/n): ")
        if stop == 'y':
            break
    '''

    numberOfPoints = int(input("How many control points? "))

    controlFreqs = np.zeros(numberOfPoints)
    controlGains = np.zeros(numberOfPoints)

    # Get the control points
    for i in range(numberOfPoints):

        controlFreqs[i] = float(input(f'Enter frequency of point {i+1}: '))
        controlGains[i] = float(input(f"Enter gain of point {i+1}: "))

    # sort 
    order = np.argsort(controlFreqs)

    controlFreqs = controlFreqs[order]
    controlGains = controlGains[order]

    # Create the linear transition function
    linearFunction = np.interp(numpyFFT.plotAxis, controlFreqs, controlGains)

    #plot linear function
    plt.figure(figsize=(10, 4))
    plt.axis((0, 2000, 0, 20))
    plt.plot(numpyFFT.plotAxis, linearFunction, 'green')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Gain')
    plt.title('Linear Transition Function')
    plt.show()

    return linearFunction

linearTransition()